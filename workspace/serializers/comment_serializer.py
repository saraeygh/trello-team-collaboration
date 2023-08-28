from rest_framework import serializers
from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import Comment


# Reza
class CommentSerializer(serializers.ModelSerializer):

    user = UserSummaryDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'task',
            'text',
            'created_at'
        ]
        read_only_fields = ('user', 'task', 'created_at')
