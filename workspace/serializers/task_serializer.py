from rest_framework import serializers

from workspace.models import Task


#Hossein
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
