from django.shortcuts import render
from news.serializers import PostSerializer
from news.models import Post
from rest_framework import viewsets, filters, generics, mixins
from drf_spectacular.utils import extend_schema_view, extend_schema


# Create your views here.

@extend_schema_view(
    get=extend_schema(summary='Получение все новостей', tags=['Новости'])
)
class PostViewSet(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
