from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, generics

from customer.models.other import FAQ
from customer.serializers.api.other import FAQSerializer


@extend_schema_view(
    get=extend_schema(summary='Часто задаваемые вопросы', tags=['FAQ'])
)
class FAQAPIList(generics.ListAPIView):
    """API FAQ - часто задаваемые вопросы и ответы на них."""
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
