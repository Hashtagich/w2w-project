from collaborations.models import Collaboration, Task
from collaborations.serializers.collaboration import CollaborationSerializer, TaskSerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Коллаборация'])
class CollaborationViewSet(viewsets.ModelViewSet):
    serializer_class = CollaborationSerializer
    queryset = Collaboration.objects.all()


@extend_schema(tags=['Задачи'])
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
