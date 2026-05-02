from __future__ import annotations

from typing import List

from django.conf import settings


class GeminiUnavailable(Exception):
    """Raised when the Gemini API call fails for any reason (network, auth, quota, etc.)."""


_model = None


def _get_model():
    """Lazily initialise the Gemini client + model."""
    global _model
    if _model is not None:
        return _model

    api_key = getattr(settings, 'GEMINI_API_KEY', '') or ''
    if not api_key:
        raise GeminiUnavailable('GEMINI_API_KEY is not configured.')

    try:
        import google.generativeai as genai
    except ImportError as exc:  # pragma: no cover
        raise GeminiUnavailable(f'google-generativeai is not installed: {exc}') from exc

    genai.configure(api_key=api_key)
    model_name = getattr(settings, 'CHATBOT_GEMINI_MODEL', 'gemini-2.5-flash')
    _model = genai.GenerativeModel(model_name)
    return _model


def get_response(messages: List[dict]) -> str:
    """Send the prepared message list to Gemini and return the assistant reply text.

    Raises GeminiUnavailable on any failure so the orchestrator can fall back gracefully.
    """
    if not messages:
        raise GeminiUnavailable('No messages provided to Gemini.')

    try:
        model = _get_model()
        # All but the last entry are seed history; the last entry is the live user turn.
        history = messages[:-1]
        latest = messages[-1]
        chat = model.start_chat(history=history)
        reply = chat.send_message(latest['parts'][0])
        text = (getattr(reply, 'text', '') or '').strip()
        if not text:
            raise GeminiUnavailable('Empty response from Gemini.')
        return text
    except GeminiUnavailable:
        raise
    except Exception as exc:  # network errors, quota, content-filter, auth, etc.
        raise GeminiUnavailable(str(exc)) from exc
