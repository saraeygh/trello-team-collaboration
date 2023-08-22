from rest_framework import serializers

from accounts.models import User
from . import ProfileSerializer


class UserDetailSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'profile',
        ]
        read_only_fields = ('username',)
