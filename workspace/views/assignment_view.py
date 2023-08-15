from rest_framework.viewsets import ModelViewSet

from workspace.models import Assignment
from workspace.serializers import AssignmentSerializer


class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return Assignment.objects.filter(task_id=task_id)

    def get_serializer_context(self):
        task_id = self.kwargs.get('task_pk')
        return {'task_id': task_id}


# class AssignmentViewSet(ModelViewSet):
#     serializer_class = AssignmentSerializer

#     def get_queryset(self):
#         return Assignment.objects.filter(task_id=self.kwargs['task_pk'])

#     def get_serializer_context(self):
#         return {
#             'task_id': self.kwargs['task_pk'],
#         }
