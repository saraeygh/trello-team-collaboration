from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from accounts.models import User
from workspace.models import Workspace, WorkspaceMember
from workspace.serializers import WorkspaceMemberSerializer
from workspace.permisssions import IsProjectAdminOrMemberReadOnly, IsProjectMember


# Mahdieh
class WorkspaceMemberViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete', 'header', 'options')

    serializer_class = WorkspaceMemberSerializer
    # permission_classes = [IsProjectMember]

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        return WorkspaceMember.objects.filter(workspace_id=workspace_id)

    def create(self, request, *args, **kwargs):
        access_level = self.request.data.get('access_level')
        if access_level not in [1, 2]:
            return Response(
                {"Error": "Select valid access level."}
            )

        try:
            workspace = Workspace.objects.get(id=self.kwargs.get('workspace_pk'))
            member = User.objects.get(id=self.request.data.get('member'))
            is_member = WorkspaceMember.objects.filter(workspace=workspace, member=member).exists()
            if is_member:
                return Response(
                {"Error": "Member already exists."}
                )
            new_member = WorkspaceMember.objects.create(
                workspace=workspace,
                member=member,
                access_level=access_level,
                )
            serializer = WorkspaceMemberSerializer(instance=new_member)
            return Response(serializer.data)

        except Workspace.DoesNotExist:
            return Response(
                {"Error": "Workspace does not exist."}
            )
        except User.DoesNotExist:
            return Response(
                {"Error": "User does not exist."}
            )
        except IntegrityError:
            return Response(
                {"Error": "Member already exists."}
            )

    def update(self, request, *args, **kwargs):
        access_level = self.request.data.get('access_level')
        if access_level not in [1, 2]:
            return Response(
                {"Error": "Select valid access level."}
            )

        try:
            workspace_member = WorkspaceMember.objects.get(id=self.kwargs.get('pk'))
        except WorkspaceMember.DoesNotExist:
            return Response(
                {"Error": "User does not exist."}
            )

        workspace_member.access_level = access_level
        workspace_member.save()
        serializer = WorkspaceMemberSerializer(instance=workspace_member)
        return Response(serializer.data)
