from rest_framework import serializers
from collaborations.models import Collaboration, Task, FotoCollaboration
from brands.serializers.other import AverageCheckSerializer, NumberSubscribersSerializer


class FotoCollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoCollaboration
        fields = ("foto",)


class TaskSerializer(serializers.ModelSerializer):
    datetime_start = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    datetime_completion = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    datetime_finish = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    datetime_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    # author =

    class Meta:
        model = Task
        fields = (
            'name',
            'status',
            'description',
            # 'author',
            'datetime_start',
            'datetime_completion',
            'datetime_finish',
            'datetime_create',
        )

    read_only_fields = ("datetime_create",)


class CollaborationSerializer(serializers.ModelSerializer):
    datetime_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    number_subscribers = NumberSubscribersSerializer()
    average_check = AverageCheckSerializer()

    collaboration_foto = FotoCollaborationSerializer(many=True)
    collaboration_task = TaskSerializer(many=True)

    class Meta:
        model = Collaboration
        fields = (
            'name',
            # 'status',
            'avatar_id',
            'description',
            'number_subscribers',
            'average_check',
            'result',
            'collaboration_foto',
            'collaboration_task',
            'datetime_create',
        )
