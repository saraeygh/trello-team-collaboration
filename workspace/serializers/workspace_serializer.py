from rest_framework import serializers
from accounts.serializers import UserSummaryDetailSerializer

from workspace.models import Workspace


# Mahdieh
class WorkspaceSerializer(serializers.ModelSerializer):

    member = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'member',
            'created_at',
        ]
