from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('who-we-help/', views.who_we_help, name='who_we_help'),
    path(
        'solutions/',
        RedirectView.as_view(pattern_name='core:who_we_help', permanent=True),
        name='solutions',
    ),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('insights/', views.insights, name='insights'),
    path('extra/', views.extra, name='extra'),
    path('privacy/', views.privacy, name='privacy'),
]
