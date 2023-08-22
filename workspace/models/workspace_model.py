from django.db import models
from django.utils.translation import gettext_lazy as _
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
    
    # def is_admin(self, user):
    #     return self.member == user and self.access_level == Workspace.Access.ADMIN

    # def is_member(self, user):
    #     return self.member == user and self.access_level == Workspace.Access.MEMBER

    # def has_member(self, user):
    #     return self.member == user

    # def get_projects(self):
    #     return self.project.all()

    # def get_admin_projects(self):
    #     return self.project.filter(access_level=Project.Access.ADMIN)

    # def get_member_projects(self):
        # return self.project.filter(access_level=Project.Access.MEMBER)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("Workspace")
        verbose_name_plural = _("Workspaces")