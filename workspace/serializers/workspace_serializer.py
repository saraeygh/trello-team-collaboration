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
            'member',
            'description',
            'created_at',
        ]
        
        read_only_fields =['member']

    # def create(self, validated_data):
    #     name = validated_data('name')
    #     description = validated_data('description')
    #     workspace = Workspace.objects.create(
    #         name=name,
    #         description=description)
        
        # return workspace