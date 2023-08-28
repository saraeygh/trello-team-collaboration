from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from workspace.models import Comment, Task
from workspace.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete', 'header', 'options')
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return Comment.objects.filter(task_id=task_id).filter(soft_delete=False)

    def get_serializer_context(self):
        task_id = self.kwargs.get('task_pk')
        return {'task_id': task_id}

    def create(self, request, *args, **kwargs):
        user = self.request.user
        task = Task.objects.get(id=self.kwargs.get('task_pk'))
        comment = Comment.objects.create(
            text=self.request.data['text'],
            user=user,
            task=task
            )
        serializer = CommentSerializer(instance=comment)
        return Response(serializer.data)
