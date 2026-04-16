from __future__ import annotations

import logging
import time

from django.conf import settings
from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


def get_client_ip(request) -> str:
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        return forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '')


def consume_rate_limit(ip_address: str) -> tuple[bool, int]:
    if not ip_address:
        return True, 0

    window = settings.RATE_LIMIT_WINDOW_SECONDS
    limit = settings.RATE_LIMIT_MAX_SUBMISSIONS
    key = f'lead-rate-limit:{ip_address}'
    now = int(time.time())
    state = cache.get(key)

    if not state or now - state['start'] > window:
        state = {'start': now, 'count': 0}

    if state['count'] >= limit:
        retry_after = max(window - (now - state['start']), 0)
        return False, retry_after

    state['count'] += 1
    cache.set(key, state, timeout=window)
    return True, 0


def send_lead_notification(lead) -> None:
    recipient = settings.LEADS_NOTIFICATION_EMAIL
    if not recipient:
        return

    context = {
        'lead': lead,
        'site_name': settings.SITE_NAME,
        'contact_email': settings.CONTACT_EMAIL,
    }
    subject = f'New lead for {settings.SITE_NAME}: {lead.name}'
    text_body = render_to_string('leads/contact_email.txt', context)
    html_body = render_to_string('leads/contact_email.html', context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient],
        reply_to=[lead.email],
    )
    email.attach_alternative(html_body, 'text/html')

    try:
        email.send(fail_silently=False)
    except Exception:
        logger.exception('Lead notification email failed to send.')
