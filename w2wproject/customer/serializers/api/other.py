from rest_framework import serializers

from customer.models import other

import random

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
        fields = '__all__'

    def to_representation(self, instance):
        instance_count = other.MagicBall.objects.count()
        if instance_count > 0:
            random_index = random.randint(0, instance_count - 1)
            random_prediction = other.MagicBall.objects.all()[random_index]
            return {'prediction': random_prediction.text}
        else:
            return {'prediction': 'No predictions available'}