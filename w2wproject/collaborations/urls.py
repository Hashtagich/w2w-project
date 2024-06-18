from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LikeViewSet, MatchViewSet, ChatViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'likes', LikeViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
