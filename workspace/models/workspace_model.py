from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeMixin
from accounts.models import User


# Mahdieh
class Workspace(TimeMixin):

    class Access(models.IntegerChoices):
        MEMBER = 1  # Can view and move only own items
        ADMIN = 2  # Can  add and remove members and modify project settings.

    name = models.CharField(
        max_length=255,
        verbose_name=_("Workspace name"),
        help_text=_('Enter the name of the workspace.')
        )

    description = models.TextField(
        blank=True, 
        null=True,
        help_text=_('Enter a description for the workspace')
        )

    member = models.ManyToManyField(
        User,
        through='WorkspaceMember', 
        through_fields=('workspace', 'member')
        )

    access_level = models.IntegerField(
        choices=Access.choices,
        default=1
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Workspace")
        verbose_name_plural = _("Workspaces")
