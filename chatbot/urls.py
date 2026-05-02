from __future__ import annotations

from django.urls import path

from . import views


app_name = 'chatbot'

urlpatterns = [
    path('start/',   views.start_session, name='chat-start'),
    path('message/', views.send_message,  name='chat-message'),
    path('history/', views.chat_history,  name='chat-history'),
    path('mode/',    views.switch_mode,   name='chat-mode'),
]
