from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from drf_spectacular.utils import extend_schema

from core.views import BaseViewSet
from workspace.models import Project, Workspace
from workspace.permissions import IsWorkspaceMemebr, HasAdminLevel
from workspace.serializers import (
    RetrieveProjectSerializer,
    CreateProjectSerializer
    )

@extend_schema(tags=["Projects"])
class WorkspaceProjectViewSet(BaseViewSet):

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsWorkspaceMemebr()]
        if self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return [IsAuthenticated(), IsWorkspaceMemebr(), HasAdminLevel()]

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        return Project.objects.\
            filter(Q(soft_delete=False) & Q(workspace_id=workspace_id)).\
            select_related("workspace").\
            prefetch_related("member")

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveProjectSerializer
        return CreateProjectSerializer

    def get_serializer_context(self):
        id = self.kwargs.get('workspace_pk')
        workspace = get_object_or_404(
            Workspace,
            id=id
        )
        return {"workspace": workspace}
