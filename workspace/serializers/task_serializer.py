from rest_framework import serializers
from workspace.serializers import RetrieveCommentSerializer
from workspace.models import Task
from accounts.serializers import UserSummaryDetailSerializer


# Hossein
class TaskSerializer(serializers.ModelSerializer):
    remaining_time = serializers.ReadOnlyField()
    is_overdue = serializers.ReadOnlyField()
    task_comments = serializers.SerializerMethodField()
    assigned_to = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "remaining_time",
            "is_overdue",
            "task_comments",
            "start_date",
            "due_date",
            "priority",
            "project",
            "assigned_to"
            ]

    def get_task_comments(self, obj):
        comments = obj.task_comments()
        comment_data = RetrieveCommentSerializer(comments, many=True).data
        return comment_data

    def validate(self, data):
        if data['start_date'] > data['end-date']:
            raise serializers.ValidationError('finish must occure after start')
        return data