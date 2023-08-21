from rest_framework import serializers

from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import WorkspaceMember
from workspace.serializers import WorkspaceSerializer


# Mahdieh
class WorkspaceMemberSerializer(serializers.ModelSerializer):

    workspace = WorkspaceSerializer()
    member = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = WorkspaceMember
        fields = [
            'id',
            'workspace',
            'member',
            'access_level', 
            'created_at'
        ]
