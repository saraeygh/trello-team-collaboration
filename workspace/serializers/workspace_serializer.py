from rest_framework import serializers
from accounts.serializers import UserSummaryDetailSerializer

from workspace.models import Workspace


# Mahdieh
class WorkspaceSerializer(serializers.ModelSerializer):

    member = UserSummaryDetailSerializer()

    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'member',
            'access_level',
            'created_at',
        ]
