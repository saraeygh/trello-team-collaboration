import re
from datetime import date
from rest_framework import serializers

from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'id',
            'gender',
            'phone',
            'birthdate',
        ]

    def validate_phone(self, value):
        iran_mobile_pattern = r"09(1[0-9]|3[0-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}"
        if re.match(iran_mobile_pattern, value):
            return value
        raise serializers.ValidationError("Not valid phone number.")

    def validate_birthdate(self, value):
        if value > date.today():
            raise serializers.ValidationError("Not Valid birthdate.")
        return value
