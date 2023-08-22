from rest_framework import serializers

from workspace.models import LabeledTask
from workspace.serializers import LabelSerializer


# Reza
class LabeledTaskSerializer(serializers.ModelSerializer):

    label = LabelSerializer()

    class Meta:
        model = LabeledTask
        fields = [
            'id',
            'task',
            'label',
        ]
