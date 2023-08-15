from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, TimeMixin
from django.utils import timezone
from accounts.models import User
from workspace.models import Project
from .comment_model import Comment


# Hossein
class Task(TimeMixin, BaseModel):

    STATUS_CHOICES = (
        ("todo", _("To Do")),
        ("doing", _("Doing")),
        ("suspend", _("Suspended")),
        ("done", _("Done")),
    )

    PRIORITY_CHOICES = (
        ('low', _('Low')),
        ('medium', _('Medium')),
        ('high', _('High')),
    )

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=250,
        help_text=_("Enter the title of the task.")
        )

    description = models.TextField(
        verbose_name=_("Description"),
        help_text="Provide a detailed description of the task."
        )

    status = models.CharField(
        verbose_name=_("Status"),
        max_length=20,
        choices=STATUS_CHOICES,
        default="todo",
        help_text="The current status of the task.\
          Choose from 'To Do', 'Doing', 'Suspended', or 'Done'."
        )

    start_date = models.DateTimeField(
        verbose_name=_("Start Date"),
        auto_now_add=True,
        help_text="The date and time when the task was created."
        )

    end_date = models.DateTimeField(
        verbose_name=_("End Date"),
        blank=True,
        null=True,
        help_text="The date and time when the task was completed."
        )

    due_date = models.DateTimeField(
        verbose_name=_("Due Date"),
        help_text="The date and time by which the task should be completed."
        )

    project = models.ForeignKey(
        Project,
        verbose_name="Project",
        on_delete=models.CASCADE,
        help_text="The project to which this task belongs."
        )

    priority = models.CharField(
        verbose_name=_("Priority"),
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium',
        help_text="The priority level of the task.\
            Choose from 'Low', 'Medium', or 'High'."
        )

    def __str__(self):
        return self.title

    def remaining_time(self):
        if self.due_date:
            return self.due_date - timezone.now()
        return None

    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now()

    def task_comments(self):
        return Comment.objects.filter(task=self)


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
        related_name='assigned_by',
        verbose_name=_("Assigned By"),
        on_delete=models.CASCADE,
        help_text="Select the user who is assigning the task."
    )

    assigned_to = models.ForeignKey(
        User,
        related_name='assigned_to',
        verbose_name=_("Assigned To"),
        on_delete=models.CASCADE,
        help_text="Select the user to whom the task is being assigned."
    )

    def __str__(self):
        return f"{self.assigned_to.username} assigned to {self.task.title}"
