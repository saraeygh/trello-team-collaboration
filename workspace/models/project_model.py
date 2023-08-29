from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, TimeMixin
from workspace.models import Workspace
from accounts.models import User


# Mahdieh
class Project(TimeMixin, BaseModel):

    name = models.CharField(
        max_length=200,
        verbose_name=_("Project name"),
        help_text=_('Enter the name of the project')
        )

    description = models.TextField(
        blank=True, null=True,
        help_text=_("Enter a description for the project.")
        )

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='project',
        help_text=_("Select the workspace this project belongs to.")
        )

    deadline = models.DateTimeField(
        verbose_name=_("Deadline"),
        blank=True,
        null=True,
        help_text="The date and time when the project deadline."
        )

    member = models.ManyToManyField(
        User,
        through='ProjectMember',
        through_fields=('project', 'member')
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
