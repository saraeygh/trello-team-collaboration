from rest_framework import serializers
from accounts.serializers import (
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
    )


# Mahdieh
class WorkspaceSerializer(serializers.ModelSerializer):

    member = UserSummaryDetailSerializer()

    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'member',
            'workspace',
            'access_level',
            'created_at',
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
            'created_at',
        ]

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        return project

# Mahdieh
class ProjectMemberSerializer(serializers.ModelSerializer):

    project = ProjectSerializer()
    member = UserSummaryDetailSerializer()
    description = serializers.CharField(max_length=500)

    class Meta:
        model = Workspace
        fields = [
            'id',
            'project',
            'description'
            'member',
            'description',
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
            'created_at'
        ]
