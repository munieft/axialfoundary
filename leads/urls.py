from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('studio/leads/', views.dashboard, name='dashboard'),
]
