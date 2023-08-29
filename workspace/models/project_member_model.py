from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, TimeMixin
from workspace.models import Project
from accounts.models import User


# Mahdieh
class ProjectMember(TimeMixin):

    project = models.ForeignKey(
        Project,
        verbose_name=_('Project'),
        related_name='project',
        on_delete=models.CASCADE,
        )

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("Users who are members of this workspace."),
        )
