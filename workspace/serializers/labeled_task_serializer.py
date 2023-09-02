from rest_framework import serializers

from workspace.models import LabeledTask
from workspace.serializers import LabelSerializer


# Reza
class RetrieveLabeledTaskSerializer(serializers.ModelSerializer):

    task = serializers.StringRelatedField()
    label = LabelSerializer()

    class Meta:
        model = LabeledTask
        fields = [
            'id',
            'task',
            'label',
        ]
