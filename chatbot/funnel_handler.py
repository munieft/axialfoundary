from __future__ import annotations

import re
from typing import Tuple

from .models import ContactLead, Session


# Ordered list of (DB field, prompt text, optional flag).
# An "optional" field can be skipped by typing "skip".
FUNNEL_STEPS = [
    ('full_name',    'What is your full name?',                                   False),
    ('email',        'What is your email address?',                               False),
    ('phone',        'Phone number? (type "skip" to continue)',                   True),
    ('company',      'Your company or organisation? (type "skip" if individual)', True),
    ('inquiry_type', 'What is this regarding? (e.g. project, pricing, partnership)', False),
    ('message',      'Briefly describe what you need help with.',                 False),
]


_EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')


def _is_skip(text: str) -> bool:
    return text.strip().lower() in {'skip', 'n/a', 'na', 'none', '-'}


def _validate(field: str, value: str) -> Tuple[bool, str]:
    """Return (is_valid, error_message). Empty error_message when valid."""
    value = value.strip()
    if field == 'full_name':
        if len(value) < 2:
            return False, 'Please share your full name so we know who to address.'
    if field == 'email':
        if not _EMAIL_RE.match(value):
            return False, 'That email looks off — could you share a valid email address?'
    return True, ''


def _next_unfilled_step(lead: ContactLead):
    """Return (field, question, optional) for the next unfilled step, or None when done."""
    for field, question, optional in FUNNEL_STEPS:
        if not getattr(lead, field, ''):
            return field, question, optional
    return None


def handle_funnel(session: Session, user_input: str) -> Tuple[str, bool]:
    """Drive the contact-collection state machine.

    Returns ``(reply_text, funnel_done)``. The orchestrator persists both the user message
    and the assistant reply for the visible conversation history.

    Behaviour:
    * On the first turn of a brand-new lead, ask the first question (we ignore whatever
      the user typed, since the first message is usually "hi" / "I want to contact you").
    * On subsequent turns, save the answer for the currently-open question, validate it,
      then ask the next question.
    * If all fields are filled, mark ``completed=True`` and confirm.
    """
    lead, created = ContactLead.objects.get_or_create(session=session, completed=False)

    if lead.completed:
        return (
            'Your enquiry has already been submitted. A team member will be in touch soon. '
            'If you need anything else, switch back to chat mode using the button above.'
        ), True

    user_input = (user_input or '').strip()

    # First turn for this lead — greet and ask the first question, regardless of what the
    # user typed (typically "hi" or "i want to contact you").
    if created and not any(getattr(lead, f, '') for f, _, _ in FUNNEL_STEPS):
        next_step = _next_unfilled_step(lead)
        if next_step is None:
            lead.completed = True
            lead.save()
            return 'Thanks! Your details are already on file.', True
        _field, question, _opt = next_step
        return (
            "Happy to help connect you with the team. I'll just collect a few quick details. "
            + question
        ), False

    # Determine which question we are answering — i.e. the first currently-empty field.
    open_step = _next_unfilled_step(lead)
    if open_step is None:
        lead.completed = True
        lead.save()
        return (
            'Thank you! Your details have been saved and a team member will contact you shortly.'
        ), True

    open_field, _open_question, optional = open_step

    if optional and _is_skip(user_input):
        # Mark as skipped by leaving blank and advancing.
        pass
    else:
        if not user_input:
            return f'Please share a value for that question. {_open_question}'.strip(), False
        valid, err = _validate(open_field, user_input)
        if not valid:
            return err, False
        setattr(lead, open_field, user_input)

    lead.save()

    # Find the next unfilled field and ask for it.
    next_step = _next_unfilled_step(lead)
    if next_step is None:
        lead.completed = True
        lead.save()
        return (
            'Thank you! Your details have been saved and a team member from Axial Foundry '
            'will contact you shortly. Anything else I can help with in the meantime?'
        ), True

    _next_field, next_question, _next_opt = next_step
    return next_question, False
