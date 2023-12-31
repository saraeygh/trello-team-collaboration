import logging
from rest_framework import serializers

from workspace.models import Assignment

logger = logging.getLogger(__name__)


# Hosein
class RetrieveAssignmentSerializer(serializers.ModelSerializer):
    assigned_by = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    task = serializers.StringRelatedField()

    class Meta:
        model = Assignment
        fields = [
            "id",
            "assigned_by",
            "assigned_to",
            "task",
        ]


class CreateAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            "id",
            "assigned_to",
        ]

    def create(self, validated_data):
        validated_data["task"] = self.context.get("task")
        validated_data["assigned_by"] = self.context.get("user")
        assignment = Assignment(**validated_data)
        assignment.save()
        logger.info(f" assigned to user success:{assignment}")
        return assignment
