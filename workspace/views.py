from rest_framework.viewsets import ModelViewSet
from .models import (
    Workspace,
    WorkspaceMember,
    Project,
    ProjectMember,
    Task,
    Assignment,
    Label,
    LabeledTask,
    Comment,
    )

from .serializers import (
    # WorkspaceSerializer,
    # WorkspaceMemberSerializer,
    # ProjectSerializer,
    # projectMemberSerializer,
    # TaskSerializer,
    # AssignmentSerializer,
    LabelSerializer,
    LabeledTaskSerializer,
    CommentSerializer,
    )


# class WorkspaceViewSet(ModelViewSet):
#     queryset = Workspace.objects.all()
#     serializer_class = WorkspaceSerializer


# class WorkspaceMemberViewSet(ModelViewSet):

#     serializer_class = WorkspaceMemberSerializer

#     def get_queryset(self):
#         return WorkspaceMember.objects.filter(workspace_id=self.kwargs['workspace_pk'])

#     def get_serializer_context(self):
#         return {'workspace_id': self.kwargs['workspace_pk']}


# class ProjectViewSet(ModelViewSet):

#     serializer_class = ProjectSerializer

#     def get_queryset(self):
#         return Project.objects.filter(workspace_id=self.kwargs['workspace_pk'])

#     def get_serializer_context(self):
#         return {'workspace_id': self.kwargs['workspace_pk']}


# class ProjectMemeberViewSet(ModelViewSet):

#     serializer_class = projectMemberSerializer

#     def get_queryset(self):
#         return ProjectMember.objects.filter(project_id=self.kwargs['project_pk'])

#     def get_serializer_context(self):
#         return {
#             'project_id': self.kwargs['project_pk'],
#             }


# class TaskViewSet(ModelViewSet):

#     serializer_class = TaskSerializer

#     def get_queryset(self):
#         return Task.objects.filter(project_id=self.kwargs['project_pk'])

#     def get_serializer_context(self):
#         return {
#             'project_id': self.kwargs['project_pk'],
#             }


# class AssignmentViewSet(ModelViewSet):

#     serializer_class = AssignmentSerializer

#     def get_queryset(self):
#         return Assignment.objects.filter(task_id=self.kwargs['task_pk'])

#     def get_serializer_context(self):
#         return {
#             'task_id': self.kwargs['task_pk'],
#             }


class LabelViewSet(ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabledTaskViewSet(ModelViewSet):
    serializer_class = LabeledTaskSerializer

    def get_queryset(self):
        return LabeledTask.objects.filter(label_id=self.kwargs['label_pk'])

    def get_serializer_context(self):
        return {'label_id': self.kwargs['label_pk']}


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_pk'])

    def get_serializer_context(self):
        return {'task_id': self.kwargs['task_pk']}
