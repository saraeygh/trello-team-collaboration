from rest_framework import serializers

from workspace.models import Workspace
from accounts.serializers import UserSummaryDetailSerializer


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
            raise serializers.ValidationError("Not valid phone number.")
        return value


# Mahdieh
class RetrieveWorkspaceSerializer(serializers.ModelSerializer):

    member = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'member',
        ]
