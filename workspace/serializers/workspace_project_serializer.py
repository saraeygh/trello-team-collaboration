from rest_framework import serializers
from datetime import date

from workspace.models import Project, Task, Workspace, ProjectMember
from workspace.serializers import WorkspaceSerializer
from accounts.serializers import UserSummaryDetailSerializer
from accounts.models import User


# Mahdieh
class WorkspaceProjectSerializer(serializers.ModelSerializer):

    workspace = serializers.StringRelatedField()
    member = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'deadline',
            'workspace',
            'member',
        ]
        read_only_fields = ("member",)