from rest_framework import serializers

from workspace.models import Project
from accounts.serializers import UserSummaryDetailSerializer


# Mahdieh
class ShortProjectSerializer(serializers.ModelSerializer):

    member = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'member']
