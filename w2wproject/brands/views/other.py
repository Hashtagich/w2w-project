from random import choice

from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes
from rest_framework.response import Response
from rest_framework.views import APIView

from brands.models.other import Predictions
from brands.serializers.other import PredictionSerializer


# Create your views here.

@extend_schema_view(
    get=extend_schema(
        summary='Получение случайного предсказания',
        tags=['Предсказания'],
        responses={200: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                'Success',
                value={'prediction': 'Ваше предсказание здесь'},
                summary='Возвращает случайное предсказание',
                description='Эндпоинт возвращает случайное предсказание из доступных.',
            ),
        ],
    )
)
class PredictionAPIView(APIView):
    def get(self, request, format=None):
        predictions = Predictions.objects.all()
        if predictions.exists():
            prediction = choice(predictions)
            serializer = PredictionSerializer(prediction)
            return Response(serializer.data)
        else:
            return Response({'prediction': 'No predictions available'})
