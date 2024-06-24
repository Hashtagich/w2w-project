from rest_framework.generics import ListAPIView
from chat.serializers import *
from chat.models import *
from brands.models import Brand
# Create your views here.


class ChatListAPIView(ListAPIView):
    serializer_class = ChatListSerializer
    queryset = Chat.objects.all()

    def get_queryset(self):
        user = self.request.user
        brand = Brand.objects.get(author=user)
        return brand.chat.all()


class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return Message.objects.filter(chat=chat_id)