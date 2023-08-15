from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeMixin
from workspace.models import Task


# Reza
class Label(TimeMixin, models.Model):
    name = models.CharField(
        verbose_name=_("Label name"),
        help_text=_("Insert label name"),
        max_length=50
        )

    task = models.ManyToManyField(
        Task,
        through='LabeledTask',
        )

    def used_count(self):
        return Task.objects.filter(label=self).count()

    def __str__(self):
        return self.name


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
