from rest_framework import serializers
from news.models import Post


class PostSerializer(serializers.ModelSerializer):
    datetime_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        model = Post
        fields = "__all__"

    read_only_fields = ("datetime_create",)
