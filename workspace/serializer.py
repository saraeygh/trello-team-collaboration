from rest_framework import serializers
from workspace.models import Task, Assignment


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    assigned_by = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    task = TaskSerializer()

    class Meta:
        model = Assignment
        fields = [
            "assigned_to",
            "task",
        ]
