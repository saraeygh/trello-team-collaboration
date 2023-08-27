from rest_framework import serializers

from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import WorkspaceMember
from workspace.serializers import WorkspaceSerializer


# Mahdieh
class WorkspaceMemberSerializer(serializers.ModelSerializer):

    workspace = WorkspaceSerializer()
    member = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = WorkspaceMember
        fields = [
            'id',
            'workspace',
            'member',
            'access_level', 
            'created_at'
        ]

    def create(self, validated_data):
        workspace_data = validated_data.pop('workspace')
        member_data = validated_data.pop('member')
        
        workspace_member = WorkspaceMember.objects.create(
            **validated_data,
            **member_data, 
            **workspace_data
            )
        for member_data in member_data:
            member_serializer = UserSummaryDetailSerializer(data=member_data)
            if member_serializer.is_valid():
                member = member_serializer.save()
                workspace_member.member.add(member)
            else:
                raise serializers.ValidationError()

        return workspace_member 
    
    #def validate(self, value):
        #if self.member < 2:
        #    raise serializers.ValidationError('Team must include 2 person or more than')
        #return value