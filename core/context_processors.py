from __future__ import annotations

from django.conf import settings
from django.urls import reverse


def site_settings(request):
    navigation = [
        {'label': 'Home', 'url': reverse('core:home')},
        {'label': 'Services', 'url': reverse('core:services')},
        {'label': 'Solutions', 'url': reverse('core:solutions')},
        {'label': 'Work', 'url': reverse('core:work')},
        {'label': 'About the Studio', 'url': reverse('core:about')},
        {'label': 'Insights', 'url': reverse('core:insights')},
        {'label': 'Contact', 'url': reverse('leads:contact')},
    ]
    return {
        'site_name': settings.SITE_NAME,
        'site_url': settings.SITE_URL,
        'contact_email': settings.CONTACT_EMAIL,
        'contact_phone': settings.CONTACT_PHONE,
        'contact_location': settings.CONTACT_LOCATION,
        'owner_profile_url': settings.OWNER_PROFILE_URL,
        'founder_name': settings.FOUNDER_NAME,
        'founder_title': settings.FOUNDER_TITLE,
        'founder_summary': settings.FOUNDER_SUMMARY,
        'site_navigation': navigation,
        'default_og_path': '/static/svg/og-card.svg',
    }
