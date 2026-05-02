from __future__ import annotations

import json
import logging
import time
from typing import Any, Dict, Optional, Tuple

from django.conf import settings

from .funnel_handler import handle_funnel
from .models import Log, Message, Session
from .retry_queue import enqueue


logger = logging.getLogger('chatbot')


def get_or_create_session(
    session_id: Optional[str],
    ip: Optional[str] = None,
    ua: Optional[str] = None,
) -> Tuple[Session, bool]:
    """Resolve a session UUID to a Session row, creating one if missing/unknown."""
    if session_id:
        try:
            return Session.objects.get(session_id=session_id), False
        except (Session.DoesNotExist, ValueError):
            pass
    session = Session.objects.create(user_ip=ip, user_agent=ua or '')
    return session, True


def _save_turn(session: Session, user_query: str, reply: str) -> None:
    """Persist a user/assistant turn pair atomically (best-effort)."""
    Message.objects.create(session=session, role='user', content=user_query)
    Message.objects.create(session=session, role='assistant', content=reply)


def handle_message(
    session_id: Optional[str],
    user_query: str,
    mode: str = 'chat',
    ip: Optional[str] = None,
    ua: Optional[str] = None,
) -> Dict[str, Any]:
    """Top-level entry point. Routes the message to either RAG chat or contact funnel,
    saves the conversation, logs the turn, and returns a JSON-ready dict for the API."""
    session, _ = get_or_create_session(session_id, ip, ua)

    # ── Contact funnel mode ─────────────────────────────────────────────────────────
    requested_funnel = mode == 'contact_funnel'
    if requested_funnel and session.mode != 'contact_funnel':
        session.mode = 'contact_funnel'
        session.save(update_fields=['mode', 'last_active'])
    if session.mode == 'contact_funnel':
        reply, done = handle_funnel(session, user_query)
        _save_turn(session, user_query, reply)
        return {
            'reply': reply,
            'session_id': str(session.session_id),
            'mode': session.mode,
            'funnel_done': done,
        }

    # ── Normal RAG chat mode ────────────────────────────────────────────────────────
    # Imports are local so a missing optional dep (e.g. chromadb) cannot break import-time
    # loading of this module — we only fail when chat is actually attempted.
    from .engine.gemini_client import GeminiUnavailable, get_response
    from .engine.prompt_builder import build_prompt
    from .engine.retriever import retrieve

    history = list(session.messages.values('role', 'content'))

    chunks = []
    try:
        chunks = retrieve(user_query)
    except Exception:
        logger.exception('Retriever failed; continuing with empty context.')

    messages = build_prompt(chunks, history, user_query)
    started = time.time()

    try:
        reply = get_response(messages)
        latency_ms = int((time.time() - started) * 1000)
        _save_turn(session, user_query, reply)
        Log.objects.create(
            session=session,
            query=user_query,
            retrieved_chunks=json.dumps(chunks, ensure_ascii=False),
            latency_ms=latency_ms,
        )
        return {
            'reply': reply,
            'session_id': str(session.session_id),
            'mode': session.mode,
        }
    except GeminiUnavailable as exc:
        latency_ms = int((time.time() - started) * 1000)
        logger.warning('Gemini unavailable for session %s: %s', session.session_id, exc)
        Log.objects.create(
            session=session,
            query=user_query,
            retrieved_chunks=json.dumps(chunks, ensure_ascii=False),
            latency_ms=latency_ms,
            gemini_error=str(exc),
        )
        # Background retry — does NOT save the user_query yet; retry_queue saves both
        # turns with is_retry=True only if it succeeds, so we don't lose the question.
        enqueue(str(session.session_id), messages, user_query)
        fallback = getattr(
            settings,
            'CHATBOT_STATIC_FALLBACK_MSG',
            'I am having a brief technical issue. Please try again in a moment.',
        )
        return {
            'reply': fallback,
            'session_id': str(session.session_id),
            'mode': session.mode,
            'error': True,
        }
