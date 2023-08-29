from rest_framework import serializers

from workspace.models import Project
from accounts.serializers import UserSummaryDetailSerializer


class CreateProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'deadline',
        ]

    def create(self, validated_data):
        validated_data['workspace'] = self.context['workspace']
        project = Project(**validated_data)
        project.save()
        return project


# Mahdieh
class RetrieveProjectSerializer(serializers.ModelSerializer):

    workspace = serializers.StringRelatedField()
    member = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'workspace',
            'description',
            'created_at',
            'member',
        ]
