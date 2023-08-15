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


# Reza
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        if workspace_id is None:
            return Project.objects.all()
        return Project.objects.filter(workspace_id=workspace_id)

    def get_serializer_context(self):
        return {
            'request': self.request,
            'workspace_id': self.kwargs.get('workspace_pk'),
            }


# Mahdieh
# class ProjectViewSet(ModelViewSet):
#     serializer_class = ProjectSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     pagination_class = DefaultPagination
#     search_fields = ['name', 'description']
#     ordering_fields = ['updated_at']

#     def get_queryset(self):
#         return Project.objects.filter(workspace_id=self.kwargs['workspace_pk'])

#     def get_serializer_context(self):
#         return {
#             'request': self.request,
#             'workspace_id': self.kwargs['workspace_pk'],
#             }

#     def destroy(self, request, pk):
#         project = get_object_or_404(Project, pk=pk)
#         if project.objects.count() > 0:
#             return Response({'error': 'project cannot be deleted because it is associated with an order item.'},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         project.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def get_permissions(self):
#         if self.request.method in ['PATCH', 'DELETE']:
#             return [IsProjectAdminOrMemberReadOnly()]
#         return [IsProjectMember()]
