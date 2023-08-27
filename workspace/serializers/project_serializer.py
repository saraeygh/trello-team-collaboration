from rest_framework import serializers

from workspace.models import Project
from workspace.serializers import WorkspaceSerializer
from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import Task

# Mahdieh
class ProjectSerializer(serializers.ModelSerializer):

    owner = UserSummaryDetailSerializer(read_only=True)
    workspace = WorkspaceSerializer()

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'owner',
            'description',
            'workspace',
            'created_at',
        ]        

    def create(self, validated_data):
        workspace_data = validated_data.pop('workspace')
        name = validated_data.pop('name')
        description = validated_data.pop('description')
        owner = validated_data.pop('owner')
        owner.save()

        project = Project.objects.create(
            name=name, 
            description=description, 
            owner=owner, 
            **workspace_data
            )
        return project

    def validate_project_id(self, project_id):
        if not Project.objects.filter(pk=project_id).exists():
            raise serializers.ValidationError(
                'No project with the given ID was found.')
        if Task.objects.filter(project_id=project_id).count() == 0:
            raise serializers.ValidationError('The project is empty.')
        return project_id