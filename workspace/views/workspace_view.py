from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from workspace.models import Workspace, WorkspaceMember
from workspace.serializers import WorkspaceMemberSerializer
from workspace.permisssions import IsProjectAdminOrMemberReadOnly, IsProjectMember


# Mahdieh
class WorkspaceViewSet(ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceMemberSerializer
    permission_classes = [IsProjectMember]
