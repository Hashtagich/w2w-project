from rest_framework import serializers

from customer.models import other


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = other.FAQ
        fields = (
            "question",
            "answer",
        )


class MagicBallSerializer(serializers.ModelSerializer):
    class Meta:
        model = other.MagicBall
        fields = (
            "prediction",
        )