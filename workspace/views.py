from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from workspace.permissions import IsProjectAdminOrMemberReadOnly
from rest_framework import generics, mixins, status
from workspace.pagination import DefaultPagination
from workspace.permissions import IsProjectMember

from .models import (
    Workspace,
    Project,
    ProjectMember,
    Task,
    Assignment,
    Label,
    LabeledTask,
    Comment,
)

from .serializers import (
    WorkspaceSerializer,
    ProjectSerializer,
    ProjectMemberSerializer,
    TaskSerializer,
    AssignmentSerializer,
    LabelSerializer,
    LabeledTaskSerializer,
    CommentSerializer,
)


# Mahdieh
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    search_fields = ['name', 'description']
    ordering_fields = ['updated_at']

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        if project.objects.count() > 0:
            return Response({'error': 'project cannot be deleted because it is associated with an order item.'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsProjectAdminOrMemberReadOnly()]
        return [IsProjectMember()]


# Mahdieh
class ProjectMemberList(mixins.ListModelMixin,
                        generics.GenericAPIView,
                        mixins.CreateModelMixin):
    serializer_class = WorkspaceSerializer
    permission_classes = [IsProjectAdminOrMemberReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        try:
            if user.is_staff:
                return Project.objects.all()

            else:
                project = Project.objects.get(pk=self.kwargs['pk'])
                query_set = WorkspaceSerializer.objects.filter(project=project)
                return query_set
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Mahdieh
class WorkspaceViewSet(ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        return Workspace.objects.filter(workspace_id=self.kwargs['workspace_pk'])

    def get_serializer_context(self):
        return {'workspace_id': self.kwargs['workspace_pk']}


class ProjectMemeberViewSet(ModelViewSet):
    serializer_class = ProjectMemberSerializer

    def get_queryset(self):
        return ProjectMember.objects.filter(project_id=self.kwargs['project_pk'])

    def get_serializer_context(self):
        return {
            'project_id': self.kwargs['project_pk'],
        }


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['project_pk'])

    def get_serializer_context(self):
        return {
            'project_id': self.kwargs['project_pk'],
        }


class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        return Assignment.objects.filter(task_id=self.kwargs['task_pk'])

    def get_serializer_context(self):
        return {
            'task_id': self.kwargs['task_pk'],
        }


class LabelViewSet(ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabledTaskViewSet(ModelViewSet):
    serializer_class = LabeledTaskSerializer

    def get_queryset(self):
        return LabeledTask.objects.filter(label_id=self.kwargs['label_pk'])

    def get_serializer_context(self):
        return {'label_id': self.kwargs['label_pk']}


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_pk'])

    def get_serializer_context(self):
        return {'task_id': self.kwargs['task_pk']}
