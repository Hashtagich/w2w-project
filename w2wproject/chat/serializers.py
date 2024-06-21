from rest_framework import serializers
from .models import Chat, Message
from brands.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'author',)


class ChatListSerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ('id', 'brands', 'created_at',)


class MessageSerializer(serializers.ModelSerializer):
    receiver = BrandSerializer(many=False, read_only=True)
    author = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'body', 'receiver', 'author', 'created_at',)