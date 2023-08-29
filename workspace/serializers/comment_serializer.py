from rest_framework import serializers
import logging

from workspace.models import Comment


logger = logging.getLogger(__name__)
class CreateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['user']
        validated_data['task'] = self.context['task']
        comment = Comment(**validated_data)
        comment.save()
        logger.info(f"new comment {Comment}")
        return comment


# Reza
class RetrieveCommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    task = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'task',
            'text',
            'created_at'
        ]
