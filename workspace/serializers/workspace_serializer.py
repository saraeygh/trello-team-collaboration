from rest_framework import serializers

from workspace.models import Workspace


# Mahdieh
class WorkspaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'created_at',
        ]

    def create(self, validated_data):
        name = validated_data('name')
        description = validated_data('description')
        workspace = Workspace.objects.create(
            name=name,
            description=description)
        
        return workspace