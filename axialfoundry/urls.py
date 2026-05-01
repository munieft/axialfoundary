from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from core import views as core_views
from core.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

admin.site.site_header = 'Axial Foundry Admin'
admin.site.site_title = 'Axial Foundry Admin'
admin.site.index_title = 'Site administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('leads.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', core_views.robots_txt, name='robots_txt'),
    path('health/', core_views.health_check, name='health_check'),
]

handler404 = 'core.views.custom_404'
