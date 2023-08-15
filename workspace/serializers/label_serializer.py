from rest_framework import serializers
from workspace.models import Label, LabeledTask


# Reza
class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = [
            'id',
            'name',
        ]


# Reza
class LabeledTaskSerializer(serializers.ModelSerializer):

    label = LabelSerializer()

    class Meta:
        model = LabeledTask
        fields = [
            'id',
            'label',
            'task',
        ]
