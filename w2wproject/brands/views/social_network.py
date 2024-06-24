from rest_framework import viewsets, filters, generics, mixins
from brands.serializers.social_network import SocialNetworkBrandSerializer
from brands.models import SocialNetwork


class SocialNetworkAPIList(generics.ListAPIView):
    serializer_class = SocialNetworkBrandSerializer
    queryset = SocialNetwork.objects.all()
