from django.urls import include, path
from rest_framework.routers import DefaultRouter
from collaborations.views.match import LikeViewSet, MatchViewSet
from collaborations.views.collaboration import CollaborationAPIList, CollaborationAPIRetrieve

router = DefaultRouter()

router.register(r'likes', LikeViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'collaborations', CollaborationViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
