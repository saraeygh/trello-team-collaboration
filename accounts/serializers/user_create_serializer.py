from django.db import transaction
from rest_framework import serializers

from accounts.serializers import ProfileSerializer
from accounts.models import User, Profile


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

            Profile.objects.create(user=user, **profile_data)
        return user

    def validate_username(self, value):
        if value in ["root", "admin"]:
            raise serializers.ValidationError("username cant be used")
        return value
