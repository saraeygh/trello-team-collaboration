from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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
        try:
            task = Task.objects.get(id=self.kwargs.get('task_pk'))
        except Task.DoesNotExist:
            return Response({"Error": "Not valid task."})
        return {
            "user": user,
            "task": task
            }
