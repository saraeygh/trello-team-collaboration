from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from workspace.paginations import DefaultPagination
from workspace.models import ProjectMember, Project
from workspace.serializers import RetrieveProjectMemberSerializer, CreateProjectMemberSerializer
from workspace.permissions import IsProjectAdminOrMemberReadOnly


# Mahdieh
class ProjectMemberViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'delete', 'header', 'options')
    #permission_classes = [IsProjectAdminOrMemberReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    ordering_fields = ['updated_at']
    serializer_class = RetrieveProjectMemberSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        return ProjectMember.objects.filter(project_id=project_id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveProjectMemberSerializer
        return CreateProjectMemberSerializer

    def get_serializer_context(self):
        try:
            project = Project.objects.get(id=self.kwargs.get('project_pk'))
        except Project.DoesNotExist:
            return Response({"Error": "Not valid project."})
        return {"project": project}
