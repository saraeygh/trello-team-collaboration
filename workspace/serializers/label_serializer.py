from django.db.utils import IntegrityError
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

    def create(self, validated_data):
        name = validated_data.pop('name')
        (label, created) = Label.objects.get_or_create(name=name)
        validated_data['label'] = label
        validated_data['task'] = self.context['task']
        try:
            labeled_task = LabeledTask(**validated_data)
            labeled_task.save()
            return label
        except IntegrityError:
            raise serializers.ValidationError("Already exists.")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            name = self.context['name']
            task = self.context['task']
            (label, created) = Label.objects.get_or_create(name=name)
            labeled_task = LabeledTask.objects.get(label=label, task=task)
            data['labeled_task_id'] = labeled_task.id
            return data
        except LabeledTask.DoesNotExist:
            return data
        except KeyError:
            return data
