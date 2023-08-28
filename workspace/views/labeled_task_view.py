from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

from workspace.serializers import LabeledTaskSerializer
from workspace.models import LabeledTask, Label


class LabeledTaskViewSet(ModelViewSet):
    serializer_class = LabeledTaskSerializer

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return LabeledTask.objects.prefetch_related("label").filter(task_id=task_id)

    def get_serializer_context(self):
        task_id = self.kwargs.get('task_pk')
        return {'task_id': task_id}

    def list(self, request, *args, **kwargs):
        if request.method == 'GET':
            raise MethodNotAllowed(request.method)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        task_id = self.kwargs.get('task_pk')
        label_id = self.kwargs.get('pk')
        try:
            labeled_task = LabeledTask.objects.get(label_id=label_id, task_id=task_id)
            serialier = LabeledTaskSerializer(instance=labeled_task)
            return Response(serialier.data)
        except LabeledTask.DoesNotExist:
            return Response(
                {
                    "Error": "There is no such task or label."
                }
            )

    def update(self, request, *args, **kwargs):
        task_id = self.kwargs.get('task_pk')
        label_id = self.kwargs.get('pk')
        try:
            labeled_task = LabeledTask.objects.get(label_id=label_id, task_id=task_id)
        except LabeledTask.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT,
                            data={
                                "Error": "There is no such task or label."
                                }
                            )

        new_label = request.data['label']['name']
        (label, created) = Label.objects.get_or_create(name=new_label)
        labeled_task.label = label
        labeled_task.save()
        serialier = LabeledTaskSerializer(instance=labeled_task)

        return Response(serialier.data)

    def partial_update(self, request, *args, **kwargs):
        task_id = self.kwargs.get('task_pk')
        label_id = self.kwargs.get('pk')
        try:
            labeled_task = LabeledTask.objects.get(label_id=label_id, task_id=task_id)
        except LabeledTask.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT,
                            data={
                                "Error": "There is no such task or label."
                                }
                            )

        new_label = request.data['label']['name']
        (label, created) = Label.objects.get_or_create(name=new_label)
        labeled_task.label = label
        labeled_task.save()
        serialier = LabeledTaskSerializer(instance=labeled_task)

        return Response(serialier.data)

    def destroy(self, request, *args, **kwargs):
        task_id = self.kwargs.get('task_pk')
        label_id = self.kwargs.get('pk')
        try:
            labeled_task = LabeledTask.objects.get(label_id=label_id, task_id=task_id)
            labeled_task.delete()
        except LabeledTask.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT,
                            data={
                                "Error": "There is no such task or label."
                                }
                            )

        return Response(status=status.HTTP_204_NO_CONTENT)
