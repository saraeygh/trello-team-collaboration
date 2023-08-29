import logging
from django.db import transaction
from rest_framework import serializers

from accounts.serializers import ProfileSerializer
from accounts.models import User, Profile

logger = logging.getLogger(__name__)



class UserCreateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'profile',
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
                }
            }

    def create(self, validated_data):
        with transaction.atomic():
            profile_data = validated_data.pop('profile')
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            logger.info(f"user {user} created.")
            Profile.objects.create(user=user, **profile_data)
            logger.info(f"A user profile created for {user}.")
        return user

    def validate_username(self, value):
        if value in ["root", "admin"]:
            logger.error(f"A user tried to set {value} as username.")
            raise serializers.ValidationError("username cant be used")
        return value
