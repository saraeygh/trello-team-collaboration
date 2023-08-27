from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from workspace.paginations import DefaultPagination
from workspace.models import Project, WorkspaceMember
from workspace.permisssions import (IsProjectAdminOrMemberReadOnly,
                                    IsProjectMember
                                    )
from workspace.serializers import (ProjectSerializer,
                                   WorkspaceSerializer,
                                   ShortProjectSerializer, WorkspaceMemberSerializer,

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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    ordering_fields = ['updated_at']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShortProjectSerializer

        return ProjectSerializer

    def get_permissions(self):
        if self.request.method in ['PUT','PATCH', 'DELETE']:
            return [IsProjectAdminOrMemberReadOnly()]
        return [IsProjectMember()]
    
    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        if workspace_id is None:
            return Project.objects.all()
        return Project.objects.filter(workspace_id=workspace_id)

    
    def create(self, request, *args, **kwargs):
        serializer = WorkspaceSerializer(
            data=request.data,
            context={'user_id': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        workspace = serializer.save()
        serializer = ProjectSerializer(workspace)
        return Response(serializer.data)
    
    
    # def put(self, request, pk):
    #     proj = get_object_or_404(Project, pk=pk)
    #     self.check_object_permissions(self.request, proj)
    #     serializer = ProjectSerializer(proj, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

