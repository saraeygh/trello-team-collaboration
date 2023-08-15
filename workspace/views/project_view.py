from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, mixins, status

from workspace.paginations import DefaultPagination
from workspace.models import Project, ProjectMember
from workspace.permisssions import (IsProjectAdminOrMemberReadOnly,
                                    IsProjectMember
                                    )
from workspace.serializers import (ProjectSerializer,
                                   WorkspaceSerializer,
                                   ProjectMemberSerializer
                                   )


# Mahdieh
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    search_fields = ['name', 'description']
    ordering_fields = ['updated_at']

    def get_queryset(self):
        return Project.objects.filter(workspace_id=self.kwargs['workspace_pk'])

    def get_serializer_context(self):
        return {
            'request': self.request,
            'workspace_id': self.kwargs['workspace_pk'],
            }

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


class ProjectMemeberViewSet(ModelViewSet):
    serializer_class = ProjectMemberSerializer

    def get_queryset(self):
        return ProjectMember.objects.filter(project_id=self.kwargs['project_pk'])

    def get_serializer_context(self):
        return {
            'project_id': self.kwargs['project_pk'],
        }
