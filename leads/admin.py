from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company',
        'email',
        'service_interest',
        'budget',
        'inquiry_type',
        'is_spam',
        'created_at',
    )
    list_filter = ('service_interest', 'budget', 'inquiry_type', 'is_spam', 'created_at')
    search_fields = ('name', 'email', 'company', 'message', 'phone')
    readonly_fields = ('created_at', 'ip_address', 'user_agent', 'referrer')
    date_hierarchy = 'created_at'
