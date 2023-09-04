import logging
from rest_framework import serializers

from workspace.models import Workspace, WorkspaceMember
from workspace.serializers import WorkspaceImageSerializer
from accounts.serializers import UserSummaryDetailSerializer

logger = logging.getLogger(__name__)


class CreateWorkspaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
        ]

    def validate_name(self, value):
        if value is None or value == "":
            logger.error(f"Invalid name -{value}- for workspace.")
            raise serializers.ValidationError("Not valid phone number.")
        return value

    def create(self, validated_data):
        workspace = super().create(validated_data)
        request = self.context['request']
        WorkspaceMember.objects.create(
            workspace=workspace,
            member=request.user,
            access_level=2,
        )
        return workspace


# Mahdieh
class RetrieveWorkspaceSerializer(serializers.ModelSerializer):

    member = UserSummaryDetailSerializer(many=True)
    images = WorkspaceImageSerializer(read_only=True)
    
    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'images',
            'created_at',
            'member',
        ]
