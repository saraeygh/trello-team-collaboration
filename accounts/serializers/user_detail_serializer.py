from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import User
from . import ProfileSerializer


class UserDetailSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
        )

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

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        if profile_data:
            profile_instance = instance.profile
            for attr, value in profile_data.items():
                setattr(profile_instance, attr, value)
            profile_instance.save()

        return super().update(instance, validated_data)
