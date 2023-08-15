from rest_framework.viewsets import ModelViewSet

from workspace.models import Task
from workspace.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['project_pk'])

    def get_serializer_context(self):
        return {
            'project_id': self.kwargs['project_pk'],
        }
