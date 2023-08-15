from rest_framework import serializers
from accounts.serializers import UserSummaryDetailSerializer
from workspace.models import Comment
from workspace.serializers import LabelSerializer


# Reza
class CommentSerializer(serializers.ModelSerializer):

    label = LabelSerializer()
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
