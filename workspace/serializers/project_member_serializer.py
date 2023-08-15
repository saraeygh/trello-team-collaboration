from rest_framework import serializers

from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import ProjectMember
from workspace.serializers import ProjectSerializer


# Mahdieh
class ProjectMemberSerializer(serializers.ModelSerializer):

    project = ProjectSerializer()
    member = UserSummaryDetailSerializer()

    class Meta:
        model = ProjectMember
        fields = [
            'id',
            'project',
            'member',
        ]
