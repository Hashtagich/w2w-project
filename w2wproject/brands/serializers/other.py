from rest_framework import serializers
from brands.models import Predictions, AverageCheck, NumberSubscribers


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = "__all__"


class BaseSerializer(serializers.ModelSerializer):
    datetime_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        abstract = True  # Это делает класс абстрактным, так что он не может быть использован самостоятельно
        fields = (
            "id",
            "name",
            "is_active",
            "datetime_create",
            "sort"
        )

    read_only_fields = ("datetime_create",)


class AverageCheckSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AverageCheck


class NumberSubscribersSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = NumberSubscribers
