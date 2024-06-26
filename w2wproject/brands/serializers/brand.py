from rest_framework import serializers
from brands.models import Brand, Interest, Category, FotoBrand, BrandInterest
from brands.serializers.other import (AverageCheckSerializer, NumberSubscribersSerializer, BaseSerializer)
from brands.serializers.social_network import SocialNetworkBrandSerializer


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

        def update(self, instance, validated_data):
            modifier_point = validated_data.pop('modifier_point', None)
            if modifier_point is not None:
                instance.modifier_up(modifier_point)
            return super().update(instance, validated_data)


class BaseBrandUpdateSerializer(serializers.Serializer):
    point = serializers.IntegerField(default=1)
    action = None

    def update(self, instance, validated_data):
        point = validated_data.get('point', 1)
        method_to_call = getattr(instance, self.action, None)
        if method_to_call:
            method_to_call(point)
        instance.save()
        return instance


class BrandModifierUpSerializer(BaseBrandUpdateSerializer):
    action = 'modifier_up'


class BrandLevelUpSerializer(BaseBrandUpdateSerializer):
    action = 'level_up'


class BrandBalanceUpSerializer(BaseBrandUpdateSerializer):
    action = 'balance_up'


class BrandExperienceUpSerializer(BaseBrandUpdateSerializer):
    action = 'experience_up'
