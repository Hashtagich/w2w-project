from rest_framework import serializers
from collaborations.models import Like, Match


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
