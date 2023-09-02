from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet

from workspace.models import ProjectMember, Project
from workspace.serializers import (
    RetrieveProjectMemberSerializer,
    CreateProjectMemberSerializer
)


# Mahdieh
class ProjectMemberViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'delete', 'header', 'options')

    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        return ProjectMember.objects.\
            filter(project_id=project_id).\
            prefetch_related("member")

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveProjectMemberSerializer
        return CreateProjectMemberSerializer

    def get_serializer_context(self):
        project = get_object_or_404(
            Project,
            id=self.kwargs.get('project_pk')
        )
        return {"project": project}
