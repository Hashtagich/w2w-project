from collaborations.models import Like, Match
from rest_framework import viewsets
from collaborations.serializers.match import LikeSerializer, MatchSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


# class ChatViewSet(viewsets.ModelViewSet):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer
#
#
# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
