import logging
from rest_framework import serializers

from workspace.models import Workspace
from workspace.serializers import WorkspaceImageSerializer
from accounts.serializers import UserSummaryDetailSerializer


logger = logging.getLogger(__name__)


class CreateWorkspaceSerializer(serializers.ModelSerializer):
    images = WorkspaceImageSerializer(read_only=True)
    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'images',
            'description',
        ]

    def validate_name(self, value):
        if value is None or value == "":
            logger.error(f"Invalid name -{value}- for workspace.")
            raise serializers.ValidationError("Not valid phone number.")
        return value


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
