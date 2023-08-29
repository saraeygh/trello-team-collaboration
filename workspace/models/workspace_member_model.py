from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeMixin
from workspace.models import Workspace
from accounts.models import User


# Mahdieh
class WorkspaceMember(TimeMixin):

    class Access(models.IntegerChoices):
        MEMBER = 1  # Can view and move only own items
        ADMIN = 2  # Can  add and remove members and modify project settings.

    workspace = models.ForeignKey(
        Workspace,
        verbose_name=_('Workspace'),
        related_name='workspace',
        on_delete=models.CASCADE,
        )

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("Users who are members of this workspace."),
        )

    access_level = models.IntegerField(
        choices=Access.choices,
        default=1
        )

    class Meta:
        unique_together = ('workspace', 'member', 'access_level')
