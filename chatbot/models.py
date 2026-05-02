from __future__ import annotations

import uuid

from django.db import models


class Session(models.Model):
    """One row per browser visitor (identified by a UUID stored in localStorage)."""

    MODE_CHOICES = [
        ('chat', 'Chat'),
        ('contact_funnel', 'Contact Funnel'),
    ]

    session_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='chat')

    class Meta:
        ordering = ['-last_active']

    def __str__(self) -> str:
        return str(self.session_id)


class Message(models.Model):
    """Full conversation history. Ordered chronologically per session."""

    ROLES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=10, choices=ROLES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_retry = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self) -> str:
        return f'{self.role} @ {self.timestamp:%Y-%m-%d %H:%M:%S}'


class Log(models.Model):
    """Observability and audit trail for every chat turn (success or failure)."""

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='logs')
    query = models.TextField()
    retrieved_chunks = models.TextField(blank=True)  # JSON-encoded list of strings
    latency_ms = models.IntegerField(default=0)
    gemini_error = models.TextField(blank=True)
    flagged = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self) -> str:
        return f'Log {self.id} — {self.timestamp:%Y-%m-%d %H:%M:%S}'


class ContactLead(models.Model):
    """Lead captured by the contact-funnel bot mode (separate from form-based leads.Lead)."""

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='contact_leads')
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=255, blank=True)
    inquiry_type = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Chatbot Contact Lead'
        verbose_name_plural = 'Chatbot Contact Leads'

    def __str__(self) -> str:
        return f'{self.full_name or "(unnamed)"} — {self.email or "no email"}'
