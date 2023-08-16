from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, TimeMixin
from workspace.models import Workspace
from accounts.models import User


# Mahdieh
class WorkspaceMember(TimeMixin, BaseModel):

    workspace = models.ForeignKey(
        Workspace,
         verbose_name=_('Workspace'),
        related_name='Workspace',
        on_delete=models.CASCADE,
        )
    
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("Users who are members of this workspace."),
        )
     
