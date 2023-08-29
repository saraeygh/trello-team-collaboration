from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from accounts.models import User
from workspace.models import Workspace, WorkspaceMember
from workspace.serializers import (
    RetrieveWorkspaceMemberSerializer,
    AddWorkspaceMemberSerializer,
    UpdateWorkspaceMemberSerializer
    )
from workspace.permisssions import IsProjectAdminOrMemberReadOnly, IsProjectMember



# Mahdieh
class WorkspaceMemberViewSet(ModelViewSet):

    # permission_classes = [IsProjectMember]

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        return WorkspaceMember.objects.filter(workspace_id=workspace_id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveWorkspaceMemberSerializer
        if self.request.method in ('PUT', 'PATCH'):
            return UpdateWorkspaceMemberSerializer
        return AddWorkspaceMemberSerializer

    def get_serializer_context(self):
        try:
            workspace = Workspace.objects.get(id=self.kwargs.get('workspace_pk'))
        except Workspace.DoesNotExist:
            return Response({"Error": "Not valid workspace."})
        return {"workspace": workspace}
