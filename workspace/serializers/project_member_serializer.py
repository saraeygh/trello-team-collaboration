from rest_framework import serializers

from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import ProjectMember


class CreateProjectMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectMember
        fields = [
            'id',
            'member',
        ]

    def create(self, validated_data):
        validated_data['project'] = self.context['project']
        try:
            project = validated_data["project"]
            member = ProjectMember.objects.get(
                member_id=validated_data["member"],
                project_id=project.id
                )
            return member
        except ProjectMember.DoesNotExist:
            member = ProjectMember(**validated_data)
            member.save()
            return member


# Mahdieh
class RetrieveProjectMemberSerializer(serializers.ModelSerializer):

    project = serializers.StringRelatedField()
    member = UserSummaryDetailSerializer()

    class Meta:
        model = ProjectMember
        fields = [
            'id',
            'project',
            'member',
        ]
