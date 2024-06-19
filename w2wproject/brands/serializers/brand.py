from rest_framework import serializers
from brands.models import Brand, Interest, Category, FotoBrand, SocialNetwork
from brands.serializers.other import (AverageCheckSerializer, NumberSubscribersSerializer, BaseSerializer)
from brands.serializers.social_network import SocialNetworkBrandSerializer


class ExperienceUpSerializer(serializers.Serializer):
    point = serializers.IntegerField()


class InterestBrandSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Interest


class CategoryBrandSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Category


class FotoBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoBrand
        fields = ("foto",)


class BrandSerializer(serializers.ModelSerializer):
    datetime_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    # author =
    number_subscribers = NumberSubscribersSerializer()
    average_check = AverageCheckSerializer()

    # collaboration =
    interests = InterestBrandSerializer(many=True)
    category = CategoryBrandSerializer(many=True)
    brand_foto = FotoBrandSerializer(many=True)
    brand_social_network = SocialNetworkBrandSerializer(many=True)

    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'status',
            'author',
            'number_subscribers',
            'average_check',
            'avatar_id',
            'value',
            'target_audience',
            'link',
            'description',
            'geo',
            'balance',
            'experience',
            'level',
            'modifier',
            'datetime_create',
            'interests',
            'category',
            'collaboration',
            'brand_foto',
            'brand_social_network',
        )
