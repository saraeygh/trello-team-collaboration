from rest_framework import serializers
from datetime import date

from workspace.models import Project, Task, Workspace, ProjectMember
from workspace.serializers import WorkspaceSerializer
from accounts.serializers import UserSummaryDetailSerializer
from accounts.models import User


# Mahdieh
class ProjectSerializer(serializers.ModelSerializer):

   # owner = UserSummaryDetailSerializer(read_only=True)
    workspace = WorkspaceSerializer()
    member = UserSummaryDetailSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            #'owner',
            'member',
            'description',
            'workspace',
            'created_at',
        ]

    def create(self, validated_data):
        workspace_data = validated_data.pop('workspace')
        member_data = validated_data.pop('member')

        project = Project.objects.create(**validated_data)

        workspace = Workspace.objects.create(**workspace_data)
        project.workspace = workspace

        for member in member_data:
            member = member.pop('user_summary_detail', None)
            project_member = ProjectMember.objects.create(project=project, **member)
            if member:
                User.objects.create(project_member=project_member, **member)

        return project
    
    def update(self, instance, validated_data):
        workspace_data = validated_data.pop('workspace', None)
        member_data = validated_data.pop('member', [])

        if workspace_data:
            # Update the nested 'profile' field if provided
            workspace_instance = instance.workspace
            for attr, value in workspace_data.items():
                setattr(workspace_instance, attr, value)
            workspace_instance.save()
        for member in member_data:
                members = member.pop('member', None)
                project_member = ProjectMember.objects.get_or_create(project=instance, **members)
                User.objects.get_or_create(project_member=project_member)

            
        return super().update(instance, validated_data)

        instance.member.clear()
    
    
        return super().update(instance, validated_data)
    # def create(self, validated_data):
    #     workspace_data = validated_data.pop('workspace')
    #     name = validated_data.pop('name')
    #     description = validated_data.pop('description')
    #     owner = User(**validated_data)
    #     member = User(**validated_data)
    #     owner.save()
    #     member.save()
    #     project = Project.objects.create(
    #         name=name,
    #         description=description,
    #         owner=owner,
    #         member=member,
    #         **workspace_data
    #         )
    #     return project

    def validate_project_id(self, project_id):
        if not Project.objects.filter(pk=project_id).exists():
            raise serializers.ValidationError(
                'No project with the given ID was found.')
        if Task.objects.filter(project_id=project_id).count() == 0:
            raise serializers.ValidationError('The project is empty.')
        return project_id
    
    def validate_deadline(self, value):
        if value < date.today():
            raise serializers.ValidationError("Not Valid deadline.")
        return value