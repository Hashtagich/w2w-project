from django.urls import path

from .views import *


urlpatterns = [
    path('chats/', ChatListAPIView.as_view()),
    path('chats/<int:chat_id>/messages/', MessageListView.as_view()),
]