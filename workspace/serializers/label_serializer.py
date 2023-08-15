from rest_framework import serializers

from workspace.models import Label
from workspace.serializers import TaskSerializer


# Reza
class LabelSerializer(serializers.ModelSerializer):

    task = TaskSerializer(many=True)

    class Meta:
        model = Label
        fields = [
            'id',
            'name',
            'task',
        ]
