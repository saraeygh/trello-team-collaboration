from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeMixin
from workspace.models import Label, Task


# Reza
class LabeledTask(TimeMixin, models.Model):
    label = models.ForeignKey(
        Label,
        verbose_name=_("Label"),
        help_text=_("Label to use"),
        on_delete=models.CASCADE,
        related_name='label',
        )

    task = models.ForeignKey(
        Task,
        verbose_name=_("Task to label"),
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return f"Label '{self.label.name}' on task '{self.task.title}'"
