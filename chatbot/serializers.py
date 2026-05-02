from __future__ import annotations

from rest_framework import serializers

from .models import ContactLead, Message, Session


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['role', 'content', 'timestamp', 'is_retry']


class SessionSerializer(serializers.ModelSerializer):
    session_id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Session
        fields = ['session_id', 'mode', 'created_at', 'last_active']


class ContactLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactLead
        fields = [
            'full_name', 'email', 'phone', 'company',
            'inquiry_type', 'message', 'completed', 'created_at',
        ]
        read_only_fields = ['completed', 'created_at']
