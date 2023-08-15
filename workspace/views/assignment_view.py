from rest_framework.viewsets import ModelViewSet

from workspace.models import Assignment
from workspace.serializers import AssignmentSerializer


class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        return Assignment.objects.filter(task_id=self.kwargs['task_pk'])

    def get_serializer_context(self):
        return {
            'task_id': self.kwargs['task_pk'],
        }
