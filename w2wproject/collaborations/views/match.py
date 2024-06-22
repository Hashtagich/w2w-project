from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from collaborations.models import Like, Match, Chat, Message
from collaborations.serializers.match import LikeSerializer, MatchSerializer, ChatSerializer, MessageSerializer


@extend_schema(tags=['Лайки'])
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


@extend_schema(tags=['Метчи'])
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


@extend_schema(tags=['Чаты'])
class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


@extend_schema(tags=['Сообщения'])
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
