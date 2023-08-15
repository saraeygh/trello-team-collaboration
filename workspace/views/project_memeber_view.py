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


class ProjectMemeberViewSet(ModelViewSet):
    serializer_class = ProjectMemberSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return ProjectMember.objects.filter(project_id=project_id)

    def get_serializer_context(self):
        project_id = self.kwargs.get('project_pk')
        return {'project_id': project_id}


# Mahdieh
# class ProjectMemberList(mixins.ListModelMixin,
#                         generics.GenericAPIView,
#                         mixins.CreateModelMixin):
#     serializer_class = WorkspaceSerializer
#     permission_classes = [IsProjectAdminOrMemberReadOnly]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def get_queryset(self):
#         user = self.request.user
#         try:
#             if user.is_staff:
#                 return Project.objects.all()

#             else:
#                 project = Project.objects.get(pk=self.kwargs['pk'])
#                 query_set = WorkspaceSerializer.objects.filter(project=project)
#                 return query_set
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# Mahdieh
# class ProjectMemeberViewSet(ModelViewSet):
#     serializer_class = ProjectMemberSerializer

#     def get_queryset(self):
#         return ProjectMember.objects.filter(project_id=self.kwargs['project_pk'])

#     def get_serializer_context(self):
#         return {
#             'project_id': self.kwargs['project_pk'],
#         }
