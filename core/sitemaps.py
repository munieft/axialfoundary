from __future__ import annotations

from django.urls import reverse
from django.contrib.sitemaps import Sitemap


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'core:home',
            'core:services',
            'core:solutions',
            'core:work',
            'core:about',
            'core:insights',
            'leads:contact',
            'core:privacy',
        ]

    def location(self, item):
        return reverse(item)
