from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views
from .views import LikeListView, MatchListView, ChatDetailView, MessageListView, MessageDetailView

router = DefaultRouter()


urlpatterns = [
    path('likes/', LikeListView.as_view(), name='like-list'),
    path('matches/', MatchListView.as_view(), name='match-list'),
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('add/', views.brand_add_view, name='brand_add'),  # URL для добавления нового бренда
    path('list/', views.brand_list_view, name='brand_list'),  # URL для списка всех брендов
    path('brands/', views.brand_list_with_likes_view, name='brand-list-with-likes'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('chat/', views.chat_detail_view, name='chat-detail'),
    path('chat/<int:match_id>/send/', views.send_message_view, name='ajax-send-message'),
    path('login/', views.login_view, name='login'),
]
