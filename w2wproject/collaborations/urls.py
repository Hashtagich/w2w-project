from django.urls import include, path
from rest_framework.routers import DefaultRouter
from collaborations.views.match import LikeViewSet, MatchViewSet, ChatViewSet, MessageViewSet
from collaborations.views.collaboration import CollaborationViewSet, TaskViewSet

router = DefaultRouter()

router.register(r'likes', LikeViewSet)
router.register(r'matches', MatchViewSet)
# router.register(r'chats', ChatViewSet)
# router.register(r'messages', MessageViewSet)
router.register(r'collaborations', CollaborationViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
