from rest_framework import serializers

from workspace.models import Project

class ShortProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id', 'name']