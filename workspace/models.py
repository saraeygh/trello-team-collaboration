from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from core.models import BaseModel, TimeMixin


# Mahdieh
class Workspace(TimeMixin, BaseModel):

    class Access(models.IntegerChoices):
        MEMBER = 1  # Can view and create and move only own items
        ADMIN = 2  # Can remove members and modify project settings.

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text='Enter the name of the workspace.'
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text='Enter a description for the workspace'
    )
    members = models.ManyToManyField(
        User,
        related_name='workspaces',
        help_text="Users who are members of this workspace.",
        on_delete=models.CASCADE
    )
    access_level = models.IntegerField(
        choices=Access.choices,
        default=1
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Mahdieh
class Project(TimeMixin, BaseModel):

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text='Enter the name of the project'
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Enter a description for the project."
    )

    # image = models.ImageField(
    #     blank=True,
    #     null=True,
    #     upload_to='board_images',
    #     help_text='Upload image to project'
    # )

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='project',
        help_text="Select the workspace this project belongs to."
    )

    def __str__(self):
        return self.name


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
        help_text="Enter the title of the task."
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
