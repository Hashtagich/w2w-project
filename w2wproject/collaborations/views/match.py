from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from collaborations.models import Like, Match
from collaborations.serializers.match import LikeSerializer, MatchSerializer


@extend_schema(tags=['Лайки'])
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


@extend_schema(tags=['Метчи'])
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
