from rest_framework import serializers
from workspace.models import Task


class TaskSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
        ]
