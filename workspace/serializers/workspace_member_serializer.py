import logging
from rest_framework import serializers

from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import WorkspaceMember

logger = logging.getLogger(__name__)


# Mahdieh
class AddWorkspaceMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkspaceMember
        fields = [
            'id',
            'member',
            'access_level',
        ]

    def validate_access_level(self, value):
        if value not in [1, 2]:
            logger.error(f"Invalid access level {value}")
            return serializers.ValidationError("Not valid access level.")
        return value

    def create(self, validated_data):
        validated_data['workspace'] = self.context['workspace']
        try:
            workspace = validated_data["workspace"]
            member = WorkspaceMember.objects.get(
                member_id=validated_data["member"],
                workspace_id=workspace.id
                )
            member.access_level = validated_data.get("access_level", 1)
            member.save()
            return member
        except WorkspaceMember.DoesNotExist:
            logger.info(f"No such memeber in workspace.")
            member = WorkspaceMember(**validated_data)
            member.save()
            logger.info(f"New member {member} added.")
            return member


class UpdateWorkspaceMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkspaceMember
        fields = [
            'access_level',
        ]

    def validate_access_level(self, value):
        if value not in [1, 2]:
            logger.error(f"Invalid access level {value}")
            return serializers.ValidationError("Not valid access level.")
        return value


# Mahdieh
class RetrieveWorkspaceMemberSerializer(serializers.ModelSerializer):

    workspace = serializers.StringRelatedField()
    member = UserSummaryDetailSerializer()

    class Meta:
        model = WorkspaceMember
        fields = [
            'id',
            'workspace',
            'member',
            'access_level',
            'created_at',
        ]
        read_only_fields = ("workspace", "created_at")
        write_only_fields = ("member", "access_level")
