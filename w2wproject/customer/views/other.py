from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models.other import FAQ, MagicBall
from customer.serializers.api.other import FAQSerializer, MagicBallSerializer

from random import choice


@extend_schema_view(
    get=extend_schema(summary='Часто задаваемые вопросы', tags=['FAQ'])
)
class FAQAPIList(generics.ListAPIView):
    """API FAQ - часто задаваемые вопросы и ответы на них."""
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"


class MagicBallAPIView(APIView):
    def get(self, request, format=None):
        predictions = MagicBall.objects.all()
        if predictions.exists():
            prediction = choice(predictions)
            serializer = MagicBallSerializer(prediction)
            return Response(serializer.data)
        else:
            return Response({'prediction': 'No predictions available'})