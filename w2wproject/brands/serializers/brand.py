from rest_framework import serializers


class ExperienceUpSerializer(serializers.Serializer):
    point = serializers.IntegerField()
