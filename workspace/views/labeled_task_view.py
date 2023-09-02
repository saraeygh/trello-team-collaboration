import logging
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from workspace.models import LabeledTask, Task
from workspace.permissions import HasTaskAccess
from workspace.serializers import (
    LabelSerializer,
    RetrieveLabeledTaskSerializer
    )


logger = logging.getLogger(__name__)


class LabeledTaskViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated, HasTaskAccess]

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return LabeledTask.objects.filter(task_id=task_id).prefetch_related("label")

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RetrieveLabeledTaskSerializer
        return LabelSerializer


    def get_serializer_context(self):
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
