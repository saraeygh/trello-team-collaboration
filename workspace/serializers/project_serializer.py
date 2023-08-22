from rest_framework import serializers

from workspace.models import Project
from workspace.serializers import WorkspaceSerializer


# Mahdieh
class ProjectSerializer(serializers.ModelSerializer):

    workspace = WorkspaceSerializer()

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'workspace',
            'created_at',
        ]

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        return project
