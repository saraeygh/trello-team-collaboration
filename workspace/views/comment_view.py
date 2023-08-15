from rest_framework.viewsets import ModelViewSet

from workspace.models import Comment
from workspace.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_pk'])

    def get_serializer_context(self):
        return {'task_id': self.kwargs['task_pk']}
