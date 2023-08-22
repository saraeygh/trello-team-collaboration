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
