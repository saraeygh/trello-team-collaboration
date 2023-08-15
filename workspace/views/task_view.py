from rest_framework.viewsets import ModelViewSet

from workspace.models import Task
from workspace.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        if project_id is None:
            return Task.objects.all()
        return Task.objects.filter(project_id=project_id)

    def get_serializer_context(self):
        return {
            'project_id': self.kwargs.get('project_pk'),
        }
