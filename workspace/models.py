from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from accounts.models import User
from core.models import TimeMixin


# Mahdieh
class Workspace(models.Model, TimeMixin):
    class Access(models.IntegerChoices):
        MEMBER = 1  # Can view and create and move only own items
        ADMIN = 2  # Can remove members and modify project settings.

    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text='Enter the name of the workspace.'
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text='Enter a description for the workspace'
    )
    user = models.ManyToManyField(
        User,
        related_name='workspaces',
        help_text="Users who are members of this workspace.",
        on_delete=models.CASCADE
    )
    access_level = models.IntegerField(
        choices=Access.choices,
        default=1
    )


# Mahdieh
class Project(models.Model):

    owner_model = models.ForeignKey(
        ContentType,
        blank=False,
        null=False,
        related_name='board',
        on_delete=models.CASCADE,
    )
    owner = GenericForeignKey(
        'owner_model',
        'owner_id'
    )
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text='Enter the name of the project'
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Enter a description for the project."
    )
    # image = models.ImageField(
    #     blank=True,
    #     null=True,
    #     upload_to='board_images',
    #     help_text='Upload image to project'
    # )
    color = models.CharField(
        blank=True,
        null=False,
        max_length=6,
        help_text='Choose color to your project.'
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='project',
        help_text="Select the workspace this project belongs to."
    )
    members = models.ManyToManyField(
        User,
        # through='Workspace',
        # through_fields=('project', 'member')
    )

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['owner_model', 'owner_id']),
        ]

