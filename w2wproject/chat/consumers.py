import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
from .serializers import *


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        self.notification_group_name = f'{self.room_name}_notification'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.send(text_data=json.dumps({'status': f'connected to room {self.room_name}'}))

    async def disconnect(self, *args, **kwargs):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        chat_id = data['chat_id']
        body = data['body']
        created_at = data['created_at']

        author = await self.get_author_brand()
        receiver = await self.get_receiver(chat_id)
        message = await self.save_message(chat_id, body, author, receiver)

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                "id": message.id,
                'chat_id': chat_id,
                'body': body,
                'author': BrandSerializer(author).data,
                'created_at': created_at
            }
        )

    async def chat_message(self, event):
        text_data = json.dumps(event)
        print(text_data)
        await self.send(text_data=json.dumps(event))

    @sync_to_async
    def get_author_brand(self):
        author = Brand.objects.get(author=self.user)
        return author

    @sync_to_async
    def get_receiver(self, chat_id):
        chat = Chat.objects.get(pk=chat_id)
        brand = Brand.objects.get(author=self.user)
        receiver = chat.brands.all()[0] if chat.brands.all()[0] != brand else chat.brands.all()[1]
        return receiver

    @sync_to_async
    def save_message(self, chat_id, body, author, receiver):
        brand = Brand.objects.get(author=self.user)
        message = Message.objects.create(chat_id=chat_id, body=body, receiver=receiver, author=brand)
        return message