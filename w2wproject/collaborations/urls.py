from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from .views import LikeViewSet, MatchViewSet, ChatViewSet, MessageViewSet

router = DefaultRouter()
# router.register(r'likes', LikeViewSet)
# router.register(r'matches', MatchViewSet)
# router.register(r'chats', ChatViewSet)
# router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from collaborations.views.collaboration import CollaborationAPIList, CollaborationAPIRetrieve

# brand
urlpatterns += [
    path('collaborations/', CollaborationAPIList.as_view(), name='collaborations'),
    path('collaboration/<int:pk>/', CollaborationAPIRetrieve.as_view(), name='collaboration'),
]
