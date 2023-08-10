from rest_framework import serializers
from accounts.models import User
from accounts.serializers import (
    UserDetailSerializer,
    UserSummaryDetailSerializer,
)
from .models import (
    Comment,
    Label,
    LabeledTask,
    Workspace,
    Project,
    Task,
    Assignment,
    WorkspaceMember,
    )


# class WorkspaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workspace
#         fields = [
#             'id',
#             'name',
#             'description',
#         ]


# class WorkspaceMemberSerializer(serializers.ModelSerializer):

#     workspace = WorkspaceSerializer()
#     member = UserSerializer()

#     class Meta:
#         model = WorkspaceMember
#         fields = [
#             'id',
#             'member',
#             'workspace',
#             'access_level',
#         ]


# class ProjectSerializer(serializers.ModelSerializer):

#     workspace = WorkspaceSerializer()

#     class Meta:
#         model = Project
#         fields = [
#             'id',
#             'name',
#             'description',
#             'workspace',
#         ]


# class projectMemberSerializer(serializers.ModelSerializer):

#     project = ProjectSerializer()
#     member = UserSerializer()

#     class Meta:
#         model = WorkspaceMember
#         fields = [
#             'id',
#             'project',
#             'member',
#         ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    assigned_by = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    task = TaskSerializer()

    class Meta:
        model = Assignment
        fields = [
            "assigned_to",
            "task",
        ]


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = [
            'id',
            'name',
        ]


class LabeledTaskSerializer(serializers.ModelSerializer):

    label = LabelSerializer()

    class Meta:
        model = LabeledTask
        fields = [
            'id',
            'label',
            'task',
        ]


class CommentSerializer(serializers.ModelSerializer):

    label = LabelSerializer()
    user = UserSummaryDetailSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'task',
            'text',
        ]
