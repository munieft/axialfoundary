from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('solutions/', views.solutions, name='solutions'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('insights/', views.insights, name='insights'),
    path('privacy/', views.privacy, name='privacy'),
]
