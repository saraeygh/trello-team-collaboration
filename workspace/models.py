from django.db import models
from core.models import BaseModel, TimeMixin
from django.utils.translation import gettext_lazy as _


# Reza
class Label(TimeMixin, BaseModel):
    name = models.CharField(
        verbose_name=_("Label name"),
        help_text=_("Insert label name"),
        max_length=50
        )

    task = models.ManyToManyField(
        "workspace.task",
        verbose_name=_("Task"),
        help_text="Task(s) with this label"
        )


# Reza
class Comment(TimeMixin, BaseModel):
    text = models.TextField(
        verbose_name=_("Comment text"),
        help_text=_("Write comment")
        )

    user = models.ForeignKey(
        "accounts.user",
        verbose_name=_("user"),
        on_delete=models.CASCADE
        )

    task = models.ForeignKey(
        "workspace.task",
        verbose_name=_("Task"),
        on_delete=models.CASCADE
        )
