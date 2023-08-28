from rest_framework import serializers

from workspace.models import Workspace
from accounts.serializers import UserSummaryDetailSerializer


# Mahdieh
class WorkspaceSerializer(serializers.ModelSerializer):

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

        read_only_fields = ('member', 'created_at')
