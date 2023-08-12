from rest_framework import serializers
from accounts.serializers import (
    UserDetailSerializer,
    UserSummaryDetailSerializer,
)
from accounts.serializers import UserSummaryDetailSerializer
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

# Mahdieh
class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
        ]

# Mahdieh
class WorkspaceMemberSerializer(serializers.ModelSerializer):

    workspace = WorkspaceSerializer()
    member = UserSummaryDetailSerializer()

    class Meta:
        model = WorkspaceMember
        fields = [
            'id',
            'member',
            'workspace',
            'access_level',
        ]


# Mahdieh
class ProjectSerializer(serializers.ModelSerializer):

    workspace = WorkspaceSerializer()

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'workspace',
        ]


# Mahdieh
class ProjectMemberSerializer(serializers.ModelSerializer):

    project = ProjectSerializer()
    member = UserSummaryDetailSerializer()

    class Meta:
        model = WorkspaceMember
        fields = [
            'id',
            'project',
            'member',
        ]


#Hossein
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


# Hosein
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

# Reza
class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = [
            'id',
            'name',
        ]

# Reza
class LabeledTaskSerializer(serializers.ModelSerializer):

    label = LabelSerializer()

    class Meta:
        model = LabeledTask
        fields = [
            'id',
            'label',
            'task',
        ]

# Reza
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
