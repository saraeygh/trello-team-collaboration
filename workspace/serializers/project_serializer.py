from rest_framework import serializers
from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import Project
from workspace.models.workspace_model import Workspace
from workspace.serializers.workspace_serializer import WorkspaceSerializer


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


# Mahdieh
class ProjectMemberSerializer(serializers.ModelSerializer):

    project = ProjectSerializer()
    member = UserSummaryDetailSerializer()
    description = serializers.CharField(max_length=500)

    class Meta:
        model = Workspace
        fields = [
            'id',
            'project',
            'description'
            'member',
            'description',
        ]
