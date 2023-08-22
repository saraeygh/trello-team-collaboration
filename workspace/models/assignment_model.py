from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeMixin
from accounts.models import User
from workspace.models import Task


# Hossein
class Assignment(TimeMixin, models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        verbose_name=_("Task"),
        help_text="Select the task that is being assigned."
    )

    assigned_by = models.ForeignKey(
        User,
        verbose_name=_("Assigned By"),
        related_name="assigned_by",
        on_delete=models.CASCADE,
        help_text="Select the user who is assigning the task."
    )

    assigned_to = models.ForeignKey(
        User,
        related_name="assigned_to",
        verbose_name=_("Assigned To"),
        on_delete=models.CASCADE,
        help_text="Select the user to whom the task is being assigned."
    )

    def is_assigned_by_user(self, user):
        return self.assigned_by == user

    def is_assigned_to_user(self, user):
        return self.assigned_to == user

    def __str__(self):
        return f"{self.assigned_to.username} assigned to {self.task.title}"
