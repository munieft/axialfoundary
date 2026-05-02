from __future__ import annotations

import logging
import threading
import time
from typing import Any, Dict, List

from django.conf import settings


logger = logging.getLogger('chatbot')

_queue: List[Dict[str, Any]] = []
_lock = threading.Lock()
_worker_running = False


def enqueue(session_id: str, messages: List[dict], user_query: str) -> None:
    """Queue a failed Gemini call for a single background retry.

    The retry runs after CHATBOT_RETRY_DELAY_SECONDS. If it succeeds, the user-turn and
    assistant-turn are both appended to the conversation with is_retry=True so the next
    page load will show the late reply. If it fails again, we just log it and move on.
    """
    global _worker_running

    with _lock:
        _queue.append({
            'session_id': session_id,
            'messages': messages,
            'user_query': user_query,
        })
        start_worker = not _worker_running
        if start_worker:
            _worker_running = True

    if start_worker:
        threading.Thread(target=_retry_worker, daemon=True).start()


def _retry_worker() -> None:
    global _worker_running
    delay = getattr(settings, 'CHATBOT_RETRY_DELAY_SECONDS', 30)
    try:
        while True:
            time.sleep(delay)
            with _lock:
                if not _queue:
                    _worker_running = False
                    return
                item = _queue.pop(0)
            _process(item)
    except Exception:  # pragma: no cover — defensive: never let the daemon crash silently
        logger.exception('Retry worker crashed')
        with _lock:
            _worker_running = False


def _process(item: Dict[str, Any]) -> None:
    from .engine.gemini_client import get_response, GeminiUnavailable
    from .models import Message, Session

    try:
        reply = get_response(item['messages'])
        session = Session.objects.get(session_id=item['session_id'])
        Message.objects.create(
            session=session,
            role='user',
            content=item['user_query'],
            is_retry=True,
        )
        Message.objects.create(
            session=session,
            role='assistant',
            content=reply,
            is_retry=True,
        )
        logger.info('Retry succeeded for session %s', item['session_id'])
    except GeminiUnavailable as exc:
        logger.warning('Retry failed for session %s: %s', item['session_id'], exc)
    except Exception:
        logger.exception('Unexpected error while processing retry for session %s', item['session_id'])
