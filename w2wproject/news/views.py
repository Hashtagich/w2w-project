from django.shortcuts import render
from news.serializers import PostSerializer
from news.models import Post
from rest_framework import viewsets, filters, generics, mixins


# Create your views here.


class PostViewSet(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
