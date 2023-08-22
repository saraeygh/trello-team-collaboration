from rest_framework import serializers

from workspace.models import Assignment
from workspace.serializers import TaskSerializer


# Hosein
class AssignmentSerializer(serializers.ModelSerializer):
    assigned_by = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    task = TaskSerializer()

    class Meta:
        model = Assignment
        fields = [
            "assigned_by",
            "assigned_to",
            "task",
        ]
