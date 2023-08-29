from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from workspace.models import Comment, Task
from workspace.serializers import CreateCommentSerializer, RetrieveCommentSerializer


# Reza
class CommentViewSet(ModelViewSet):
    serializer_class = RetrieveCommentSerializer

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return Comment.objects.filter(soft_delete=False).filter(task_id=task_id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveCommentSerializer
        return CreateCommentSerializer

    def get_serializer_context(self):
        user = self.request.user
        task = get_object_or_404(Task, id=self.kwargs.get('task_pk'))
        return {
            "user": user,
            "task": task
            }
