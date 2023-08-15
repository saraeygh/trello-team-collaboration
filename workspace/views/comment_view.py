from rest_framework.viewsets import ModelViewSet

from workspace.models import Comment
from workspace.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return Comment.objects.filter(task_id=task_id)

    def get_serializer_context(self):
        task_id = self.kwargs.get('task_pk')
        return {'task_id': task_id}
