from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from workspace.models import Assignment, Task
from workspace.serializers import (
    RetrieveAssignmentSerializer,
    CreateAssignmentSerializer
    )


# Hossein
class AssignmentViewSet(ModelViewSet):
    http_method_names = ["get", "post", "delete", "header", "options"]

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return Assignment.objects.filter(task_id=task_id)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RetrieveAssignmentSerializer
        return CreateAssignmentSerializer

    def get_serializer_context(self):
        task_id = self.kwargs.get("task_pk")
        user = self.request.user
        task = get_object_or_404(Task, id=task_id)
        return {
            "task": task,
            "user": user
        }
