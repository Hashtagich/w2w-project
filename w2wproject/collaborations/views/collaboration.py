from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collaborations.models import Collaboration
from collaborations.serializers.collaboration import CollaborationSerializer
from rest_framework import viewsets, filters, generics, mixins
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    get=extend_schema(summary='Получение коллаборации по её ID', tags=['Коллаборация'])
)
class CollaborationAPIRetrieve(generics.RetrieveAPIView):
    serializer_class = CollaborationSerializer
    queryset = Collaboration.objects.all()


@extend_schema_view(
    get=extend_schema(summary='Получение всех коллабораций', tags=['Коллаборация'])
)
class CollaborationAPIList(generics.ListAPIView):
    serializer_class = CollaborationSerializer
    queryset = Collaboration.objects.all()
