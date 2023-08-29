from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from workspace.models import Task, Project
from workspace.serializers import (
    RetrieveTaskSerializer,
    CreateTaskSerializer
)


# Hossein
class TaskViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete", "header", "options"]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')

        return Task.objects.filter(soft_delete=False).\
            filter(project_id=project_id)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RetrieveTaskSerializer
        return CreateTaskSerializer

    def get_serializer_context(self):
        project = get_object_or_404(
            Project,
            id=self.kwargs.get('project_pk')
        )
        return {"project": project}   


# Hossein
class TaskViewSetNone(ModelViewSet):
    http_method_names = ["header", "options"]

    queryset = Task.objects.all()
    serializer_class = RetrieveTaskSerializer
