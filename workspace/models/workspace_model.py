from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeMixin, BaseModel
from accounts.models import User


# Mahdieh
class Workspace(TimeMixin, BaseModel):

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

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("Users who are members of this workspace."),
        )

    access_level = models.IntegerField(
        choices=Access.choices,
        default=1
        )

    def __str__(self):
        return f'{self.member.first_name}, {self.member.last_name} , {self.project.name}'
