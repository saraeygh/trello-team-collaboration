from django.db import transaction
from rest_framework import serializers

from workspace.models import LabeledTask, Label, Task
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
        read_only_fields = ('task',)

    def create(self, validated_data):
        with transaction.atomic():
            task = Task.objects.get(id=self.context.get('task_id'))
            label_name = validated_data['label']['name']
            (label, created) = Label.objects.update_or_create(name=label_name)
            (labeled_task, updated) = LabeledTask.objects.update_or_create(task=task, label=label)

        return labeled_task
