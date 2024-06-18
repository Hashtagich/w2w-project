from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from news.views import PostViewSet

router = DefaultRouter()

urlpatterns = [
    path('news/', PostViewSet.as_view(), name='news'),
]
