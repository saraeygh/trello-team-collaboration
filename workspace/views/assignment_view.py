from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from workspace.models import Assignment, Task
from workspace.permissions import HasTaskAccess
from workspace.serializers import (
    RetrieveAssignmentSerializer,
    CreateAssignmentSerializer
    )


# Hossein
@extend_schema(tags=["Assignments"])
class AssignmentViewSet(ModelViewSet):
    http_method_names = ["get", "post", "delete", "header", "options"]
    permission_classes = [IsAuthenticated, HasTaskAccess]

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return Assignment.objects.filter(task_id=task_id).\
            select_related('assigned_by').\
            select_related('assigned_to')

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RetrieveAssignmentSerializer
        return CreateAssignmentSerializer

    def get_serializer_context(self):
        task_id = self.kwargs.get("task_pk")
        task = get_object_or_404(Task, id=task_id)
        user = self.request.user
        return {
            "task": task,
            "user": user
        }
