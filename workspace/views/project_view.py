from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, mixins, status
from django.db.models import Case, When

from workspace.paginations import DefaultPagination
from workspace.models import Project, ProjectMember, Workspace
from workspace.permisssions import (IsProjectAdminOrMemberReadOnly,
                                    IsProjectMember
                                    )
from workspace.serializers import (ProjectSerializer,
                                   WorkspaceSerializer,
                                   ProjectMemberSerializer
                                   )


# # Reza
# class ProjectViewSet(ModelViewSet):
#     serializer_class = ProjectSerializer
#
#     def get_queryset(self):
#         workspace_id = self.kwargs.get('workspace_pk')
#         if workspace_id is None:
#             return Project.objects.all()
#         return Project.objects.filter(workspace_id=workspace_id)
#
#     def get_serializer_context(self):
#         return {
#             'request': self.request,
#             'workspace_id': self.kwargs.get('workspace_pk'),
#             }


# Mahdieh
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    search_fields = ['name', 'description']
    ordering_fields = ['updated_at']

    def get_queryset(self):
        # Sort by access_level so projects where you're admin at top
        project_ids = Workspace.objects.filter(
            member=self.request.user).\
                order_by('-access_level').\
                    values_list('project__id', flat=True)

        preserved = Case(*[When(pk=pk, then=pos)
                           for pos, pk in enumerate(project_ids)])
        return Project.objects.filter(pk__in=project_ids).order_by(preserved)
    

    def get_serializer_context(self):
         return {
             'request': self.request,
             'workspace_id': self.kwargs.get('workspace_pk'),
             }




