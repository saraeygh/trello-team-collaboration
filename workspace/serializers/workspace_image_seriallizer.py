from rest_framework import serializers
from workspace.models import WorkspaceImage


# Mahdieh
class WorkspaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceImage
        fields = ['id', 'image']
    
    def create(self, validated_data):
        workspace_id = self.context['workspace_id']
        return WorkspaceImage.objects.create(
            workspace_id=workspace_id, 
            **validated_data)
   