from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, TimeMixin

from accounts.models import User


# Reza
class Comment(TimeMixin, BaseModel):
    text = models.TextField(
        verbose_name=_("Comment text"),
        help_text=_("Write comment")
        )

    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE
        )

    task = models.ForeignKey(
        "workspace.Task",
        verbose_name=_("Task"),
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.text
