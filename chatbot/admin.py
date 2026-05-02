from __future__ import annotations

from django.contrib import admin

from .models import ContactLead, Log, Message, Session


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('role', 'content', 'timestamp', 'is_retry')
    can_delete = False
    show_change_link = False


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'mode', 'user_ip', 'created_at', 'last_active')
    list_filter = ('mode', 'created_at')
    search_fields = ('session_id', 'user_ip', 'user_agent')
    readonly_fields = ('session_id', 'created_at', 'last_active')
    inlines = [MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'role', 'short_content', 'is_retry', 'timestamp')
    list_filter = ('role', 'is_retry', 'timestamp')
    search_fields = ('content', 'session__session_id')
    readonly_fields = ('session', 'role', 'content', 'timestamp', 'is_retry')

    @admin.display(description='Content')
    def short_content(self, obj: Message) -> str:
        return (obj.content[:80] + '…') if len(obj.content) > 80 else obj.content


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('session', 'short_query', 'latency_ms', 'has_error', 'flagged', 'timestamp')
    list_filter = ('flagged', 'timestamp')
    search_fields = ('query', 'session__session_id')
    readonly_fields = ('session', 'query', 'retrieved_chunks', 'latency_ms', 'gemini_error', 'timestamp')

    @admin.display(description='Query')
    def short_query(self, obj: Log) -> str:
        return (obj.query[:80] + '…') if len(obj.query) > 80 else obj.query

    @admin.display(boolean=True, description='Error')
    def has_error(self, obj: Log) -> bool:
        return bool(obj.gemini_error)


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'company', 'inquiry_type', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'company', 'message')
    readonly_fields = ('session', 'created_at')
