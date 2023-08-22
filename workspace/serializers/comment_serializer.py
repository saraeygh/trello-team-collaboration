from rest_framework import serializers
from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import Comment


# Reza
class CommentSerializer(serializers.ModelSerializer):

    user = UserSummaryDetailSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'task',
            'text',
            'created_at'
        ]
