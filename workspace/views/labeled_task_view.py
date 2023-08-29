from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import logging
from workspace.serializers import LabelSerializer, RetrieveLabeledTaskSerializer
from workspace.models import LabeledTask, Task


logger = logging.getLogger(__name__)
class LabeledTaskViewSet(ModelViewSet):

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return LabeledTask.objects.prefetch_related("label").filter(task_id=task_id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveLabeledTaskSerializer
        return LabelSerializer

    def get_serializer_context(self, *args, **kwargs):
        try:
            name = self.request.data["name"]
        except KeyError:
            logger.error('invalid name for task')
            return Response({"Error": "Not valid name."})
        task = get_object_or_404(
            Task,
            id=self.kwargs.get('task_pk')
        )
        return {
            "task": task,
            "name": name,
            }
