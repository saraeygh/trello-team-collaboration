import re
import logging
from datetime import date
from rest_framework import serializers

from accounts.models import Profile

logger = logging.getLogger(__name__)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'id',
            'gender',
            'phone',
            'birthdate',
            'image',
        ]

    def validate_phone(self, value):
        iran_mobile_pattern = r"09(1[0-9]|3[0-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}"
        if re.match(iran_mobile_pattern, value):
            return value
        logger.error(f"Invalid phone number {value}.")
        raise serializers.ValidationError("Not valid phone number.")
