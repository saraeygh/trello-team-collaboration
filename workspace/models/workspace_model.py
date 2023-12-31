from django.db import models
from django.utils.translation import gettext_lazy as _

from workspace.validators import validate_file_size
from core.models import TimeMixin, BaseModel
from accounts.models import User


# Mahdieh
class Workspace(TimeMixin, BaseModel):

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
        )

    image = models.ImageField(
        upload_to='workspace/images',
        null=True,
        blank=True,
        validators=[validate_file_size],
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("Workspace")
        verbose_name_plural = _("Workspaces")
