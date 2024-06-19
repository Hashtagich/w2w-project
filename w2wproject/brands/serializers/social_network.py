from rest_framework import serializers
from brands.models import SocialNetwork, NameSocialNetwork
from brands.serializers.other import BaseSerializer
from brands.serializers.brand import BrandSerializer


class NameSocialNetworkSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = NameSocialNetwork


class SocialNetworkBrandSerializer(serializers.ModelSerializer):
    datetime_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    name = NameSocialNetworkSerializer()
    brand_id = BrandSerializer()

    class Meta:
        model = SocialNetwork
        fields = (
            'id',
            'name',
            'link',
            'datetime_create',
            'brand_id',
        )
