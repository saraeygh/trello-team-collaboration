from rest_framework import serializers

from accounts.models import User


class UserSummaryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'full_name',
            'username',
            'email',
        ]
        read_only_fields = (
            'full_name',
            'username',
            'email',
            )
