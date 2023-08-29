from rest_framework import serializers
import logging
from workspace.models import Task
from accounts.serializers import UserSummaryDetailSerializer
from datetime import datetime

logger = logging.getLogger(__name__)
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
    # start_date = serializers.DateTimeField()
    # end_date = serializers.DateTimeField()

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
        
    def validate_end_date(self, value):
        date_format = "YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]"
        try:
            datetime.strptime(value, date_format)
        except ValueError:
            logger.error(f"invalid datetime or format{Task}")
            raise serializers.ValidationError("invalid datetime field")
        return value    

    def validate(self, attrs):
        try:
            start_date = attrs["start_date"]
            end_date = attrs["end_date"]
        except KeyError:
            return attrs
        if start_date > end_date:
            logger.error(f"finish must occur after start{Task}")
            raise serializers.ValidationError('finish must occur after start')

    def create(self, validated_data):
        validated_data["project"]=self.context["project"]
        task = Task(**validated_data)
        task.save()
        logger.info(f"task created:{Task}")
        return task
