from django.db.utils import IntegrityError
from rest_framework import serializers
import logging

from workspace.models import Label, LabeledTask

logger = logging.getLogger(__name__)


# Reza
class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = [
            'id',
            'name',
        ]

    def create(self, validated_data):
        name = validated_data.pop('name')
        (label, created) = Label.objects.get_or_create(name=name)
        validated_data['label'] = label
        validated_data['task'] = self.context['task']
        try:
            labeled_task = LabeledTask(**validated_data)
            labeled_task.save()
            logger.info(f"new label {Label}" )
            return label
        except IntegrityError:
            logger.error('label already exists.')
            raise serializers.ValidationError("Already exists.")

    def update(self, instance, validated_data):
        name = validated_data.pop('name')
        (label, created) = Label.objects.get_or_create(name=name)
        validated_data['label'] = label
        validated_data['task'] = self.context['task']
        try:
            labeled_task = LabeledTask(**validated_data)
            labeled_task.save()
            logger.info(f"new label {Label}" )
            return label
        except IntegrityError:
            logger.error('label already exists.')
            raise serializers.ValidationError("Already exists.")
