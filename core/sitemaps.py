from __future__ import annotations

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """Sitemap for Axial Foundry's public commercial pages.

    Intentionally excluded:
      - core:solutions — 301 redirects to core:who_we_help
      - core:insights — hidden from navigation and noindex-ed
      - core:extra    — internal holding page; not part of the commercial site
    """

    protocol = 'https'

    priority_map = {
        'core:home': 1.0,
        'core:services': 0.9,
        'core:who_we_help': 0.8,
        'core:work': 0.85,
        'core:about': 0.7,
        'leads:contact': 0.95,
        'core:privacy': 0.2,
    }

    changefreq_map = {
        'core:home': 'weekly',
        'core:services': 'monthly',
        'core:who_we_help': 'monthly',
        'core:work': 'monthly',
        'core:about': 'monthly',
        'leads:contact': 'monthly',
        'core:privacy': 'yearly',
    }

    def items(self) -> list[str]:
        return [
            'core:home',
            'core:services',
            'core:who_we_help',
            'core:work',
            'core:about',
            'leads:contact',
            'core:privacy',
        ]

    def location(self, item: str) -> str:
        return reverse(item)

    def priority(self, item: str) -> float:
        return self.priority_map.get(item, 0.5)

    def changefreq(self, item: str) -> str:
        return self.changefreq_map.get(item, 'monthly')
