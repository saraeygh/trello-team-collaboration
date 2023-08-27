from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404

from workspace.paginations import DefaultPagination
from workspace.models import WorkspaceMember, Project, Workspace
from workspace.serializers import WorkspaceMemberSerializer, ProjectMemberSerializer
from workspace.permisssions import IsProjectAdminOrMemberReadOnly

# Mahdieh
class ProjectMemberViewSet(ModelViewSet):
    permission_classes = [IsProjectAdminOrMemberReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    ordering_fields = ['updated_at']
    serializer_class = ProjectMemberSerializer
    
    def get_queryset(self):
        try:
            project = Project.objects.get(pk=self.kwargs['pk'])
            query_set = Workspace.objects.filter(project=project)
        except:
            raise Http404 
        return query_set
    
    def get_serializer_context(self):
        project_id = self.kwargs.get('project_pk')
        return {'project_id': project_id}
    
    def get_object(self, pk):
        obj = get_object_or_404(WorkspaceMember, pk=pk)
        self.check_object_permissions(self.request, obj.project)
        return obj

    def put(self, request, pk):
        pmem = self.get_object(pk)
        serializer = WorkspaceMemberSerializer(
            pmem, 
            data=request.data, 
            context={"request": request}
            )
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





#class ProjectMemeberViewSet(ModelViewSet):
#    serializer_class = ProjectMemberSerializer
#
#    def get_queryset(self):
#        project_id = self.kwargs.get('project_pk')
#        return ProjectMember.objects.filter(project_id=project_id)

#    def get_serializer_context(self):
#        project_id = self.kwargs.get('project_pk')
#        return {'project_id': project_id}



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
