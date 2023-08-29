from rest_framework import serializers

from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import WorkspaceMember
from workspace.serializers import RetrieveWorkspaceSerializer


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
            return serializers.ValidationError("Not valid access level.")
        return value

    def create(self, validated_data):
        validated_data['workspace'] = self.context['workspace']
        try:
            workspace=validated_data["workspace"]
            member = WorkspaceMember.objects.get(
                member_id=validated_data["member"],
                workspace_id=workspace.id
                )
            member.access_level = validated_data.get("access_level", 1)
            member.save()
            return member
        except WorkspaceMember.DoesNotExist:
            member = WorkspaceMember(**validated_data)
            member.save()
            return member


class UpdateWorkspaceMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkspaceMember
        fields = [
            'access_level',
        ]

    def validate_access_level(self, value):
        if value not in [1, 2]:
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
