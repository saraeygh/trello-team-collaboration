from rest_framework import serializers
from workspace.serializers import RetrieveCommentSerializer
from workspace.models import Task
from accounts.serializers import UserSummaryDetailSerializer


# Hossein
class RetrieveTaskSerializer(serializers.ModelSerializer):
    remaining_time = serializers.ReadOnlyField()
    is_overdue = serializers.ReadOnlyField()
    assigned_to = UserSummaryDetailSerializer(many=True)
    project = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "remaining_time",
            "is_overdue",
            "start_date",
            "due_date",
            "priority",
            "project",
            "assigned_to"
            ]


class CreateTaskSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "start_date",
            "due_date",
            "end_date",
            "priority",
            ]

    def validate(self, data):
        try:
            start_date = data["start_date"]
            end_date = data["end_date"]
        except KeyError:
            return data    
        if start_date > end_date:
            raise serializers.ValidationError('finish must occur after start')
    
    def create(self, validated_data):
        validated_data["project"]=self.context["project"]
        task = Task(**validated_data)
        task.save()
        return task