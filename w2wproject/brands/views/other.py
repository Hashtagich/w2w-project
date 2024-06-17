from brands.serializers.other import PredictionSerializer
from brands.models.other import Predictions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from random import choice


# Create your views here.


class PredictionViewSet(generics.ListAPIView):
    serializer_class = PredictionSerializer
    queryset = Predictions.objects.all()


class PredictionAPIView(APIView):
    def get(self, request, format=None):
        predictions = Predictions.objects.all()
        if predictions.exists():
            prediction = choice(predictions)
            serializer = PredictionSerializer(prediction)
            return Response(serializer.data)
        else:
            return Response({'prediction': 'No predictions available'})
