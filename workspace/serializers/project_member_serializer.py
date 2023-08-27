from rest_framework import serializers

from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import ProjectMember, Workspace
from workspace.serializers import ProjectSerializer, WorkspaceSerializer
from accounts.models import User


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

    def create(self, validated_data):
        project_data = validated_data.pop('project')
        member = User(**validated_data)
        member.save()

        project = ProjectMember.objects.create(user=member, **project_data)
        return project
    
    def get_members(self, obj):
        queryset = Workspace.objects.filter(project=obj)
        return WorkspaceSerializer(
            queryset, 
            many=True, 
            context={"request": self.context['request']}).data
