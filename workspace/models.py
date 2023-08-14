from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, TimeMixin
from accounts.models import User
from django.utils import timezone


# Mahdieh
class Workspace(TimeMixin):

    class Access(models.IntegerChoices):
        MEMBER = 1  # Can view and move only own items
        ADMIN = 2  # Can  add and remove members and modify project settings.
    id = models.IntegerField(primary_key=True)
    
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
    
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("Users who are members of this workspace."),
        )

    access_level = models.IntegerField(
        choices=Access.choices,
        default=1
        )

    def __str__(self):
        return f'{self.member.first_name}, {self.member.last_name} , {self.project.name}'

        
# Mahdieh
class Project(TimeMixin, BaseModel):
    name = models.CharField(
        max_length=200,
        verbose_name=_("Project name"),
        help_text=_('Enter the name of the project')
        )

    description = models.TextField(
        blank=True, null=True,
        help_text=_("Enter a description for the project.")
        )

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='project',
        help_text=_("Select the workspace this project belongs to.")
        )

    deadline = models.DateTimeField(
        verbose_name=_("Deadline"),
        blank=True,
        null=True,
        auto_now_add=True,
        help_text="The date and time when the project deadline."
        )

    member = models.ManyToManyField(
        User,
        through='ProjectMember', 
        through_fields=('project', 'member')
        )

    #slug = models.SlugField(
    #    max_length=50,
    #    unique=True
    #    )
        
    def __str__(self):
        return self.name


# Mahdieh
class ProjectMember(TimeMixin, BaseModel):

    project = models.ForeignKey(
        Project,
        verbose_name=_('Project'),
        related_name='project',
        on_delete=models.CASCADE,
        )

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("Users who are members of this workspace."),
        )


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


# Reza
class Label(TimeMixin, models.Model):
    name = models.CharField(
        verbose_name=_("Label name"),
        help_text=_("Insert label name"),
        max_length=50
        )

    def __str__(self):
        return self.name


# Reza
class LabeledTask(TimeMixin, models.Model):
    label = models.ForeignKey(
        Label,
        verbose_name=_("Label"),
        help_text=_("Label to use"),
        on_delete=models.CASCADE
        )

    task = models.ForeignKey(
        Task,
        verbose_name=_("Task to label"),
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f"Label ({self.label.name}) on task ({self.task.title})"


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
        "workspace.task",
        verbose_name=_("Task"),
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.text
