from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "invalid data"})
        return {
            "task": task,
            "user": user
        }
