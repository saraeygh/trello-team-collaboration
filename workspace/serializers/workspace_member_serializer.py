from rest_framework import serializers

from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import ProjectMember
from workspace.serializers import WorkspaceSerializer


# Mahdieh
class WorkspaceMemberSerializer(serializers.ModelSerializer):

    workspace = WorkspaceSerializer()
    member = UserSummaryDetailSerializer()

    class Meta:
        model = ProjectMember
        fields = [
            'id',
            'Workspace',
            'member',
        ]
