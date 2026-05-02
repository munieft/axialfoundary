from __future__ import annotations

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Session
from .services import handle_message


def _client_ip(request) -> str:
    """Return the best-guess client IP, honouring X-Forwarded-For when present."""
    xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '') or ''


@api_view(['POST'])
def start_session(request):
    """POST /api/chat/start/ → {"session_id": "<uuid>"}."""
    ip = _client_ip(request)
    ua = request.META.get('HTTP_USER_AGENT', '')[:1000]
    session = Session.objects.create(user_ip=ip or None, user_agent=ua)
    return Response({'session_id': str(session.session_id), 'mode': session.mode})


@api_view(['POST'])
def send_message(request):
    """POST /api/chat/message/ {"session_id", "message", "mode"?} → {"reply", ...}."""
    session_id = request.data.get('session_id')
    message = (request.data.get('message') or '').strip()
    mode = request.data.get('mode') or 'chat'

    if not message:
        return Response(
            {'error': 'message is required'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if len(message) > 2000:
        return Response(
            {'error': 'message too long (max 2000 characters)'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if mode not in {'chat', 'contact_funnel'}:
        mode = 'chat'

    ip = _client_ip(request)
    ua = request.META.get('HTTP_USER_AGENT', '')[:1000]
    data = handle_message(session_id, message, mode=mode, ip=ip or None, ua=ua)
    return Response(data)


@api_view(['GET'])
def chat_history(request):
    """GET /api/chat/history/?session_id=<uuid> → {"messages": [...]}."""
    sid = request.query_params.get('session_id')
    if not sid:
        return Response({'messages': []})
    try:
        session = Session.objects.get(session_id=sid)
    except (Session.DoesNotExist, ValueError):
        return Response({'messages': []})
    messages = list(session.messages.values('role', 'content', 'timestamp', 'is_retry'))
    return Response({
        'messages': messages,
        'session_id': str(session.session_id),
        'mode': session.mode,
    })


@api_view(['POST'])
def switch_mode(request):
    """POST /api/chat/mode/ {"session_id", "mode"} → {"status", "mode"}."""
    sid = request.data.get('session_id')
    mode = request.data.get('mode') or 'chat'
    if mode not in {'chat', 'contact_funnel'}:
        return Response(
            {'error': 'mode must be "chat" or "contact_funnel"'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        session = Session.objects.get(session_id=sid)
    except (Session.DoesNotExist, ValueError):
        return Response(
            {'error': 'session not found'},
            status=status.HTTP_404_NOT_FOUND,
        )
    session.mode = mode
    session.save(update_fields=['mode', 'last_active'])
    return Response({'status': 'ok', 'mode': mode})
