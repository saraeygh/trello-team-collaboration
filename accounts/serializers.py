from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer
    )
from rest_framework import serializers

from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'phone',
            'birthdate',
            'gender',
        ]


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'birthdate',
            'gender',
        ]
        read_only_fields = ('username',)


class UserSummaryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
        ]
        read_only_fields = (
            'first_name',
            'username',
            'email',
            )