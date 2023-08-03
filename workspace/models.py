from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from accounts.models import User
from core.models import TimeMixin, BaseModel


# Mahdieh
class Workspace(TimeMixin, BaseModel):
    class Access(models.IntegerChoices):
        MEMBER = 1  # Can view and create and move only own items
        ADMIN = 2  # Can remove members and modify project settings.

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text='Enter the name of the workspace.'
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text='Enter a description for the workspace'
    )
    members = models.ManyToManyField(
        User,
        related_name='workspaces',
        help_text="Users who are members of this workspace.",
        on_delete=models.CASCADE
    )
    access_level = models.IntegerField(
        choices=Access.choices,
        default=1
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Mahdieh
class Project(TimeMixin, BaseModel):

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
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='project',
        help_text="Select the workspace this project belongs to."
    )

    def __str__(self):
        return self.name



