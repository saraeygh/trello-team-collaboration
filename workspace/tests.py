from django.test import TestCase
from django.utils import timezone
from .models import Project, Task, Assignment, Comment, Label, LabeledTask, Workspace
from accounts.models import User


class ModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user1", email="user1@gmail.com")
        self.user2 = User.objects.create(username="user2", email="user2@gmail.com")
        self.workspace = Workspace.objects.create(name="Test Workspace")

    def test_create_project(self):
        project = Project.objects.create(name="Test Project", workspace=self.workspace)
        self.assertEqual(str(project), "Test Project")

    def test_create_task(self):
        project = Project.objects.create(name="Test Project", workspace=self.workspace)
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            status="todo",
            project=project,
            due_date=timezone.now() + timezone.timedelta(days=7),
        )
        self.assertEqual(str(task), "Test Task")

    def test_create_assignment(self):
        project = Project.objects.create(name="Test Project", workspace=self.workspace)
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            status="todo",
            project=project,
            due_date=timezone.now() + timezone.timedelta(days=7),
        )
        assignment = Assignment.objects.create(
            task=task, assigned_by=self.user1, assigned_to=self.user2
        )
        self.assertTrue(assignment.is_assigned_by_user(self.user1))
        self.assertTrue(assignment.is_assigned_to_user(self.user2))

    def test_create_comment(self):
        project = Project.objects.create(name="Test Project", workspace=self.workspace)
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            status="todo",
            project=project,
            due_date=timezone.now() + timezone.timedelta(days=7),
        )
        comment = Comment.objects.create(user=self.user1, task=task, text="Test comment")
        self.assertEqual(str(comment), "Test comment")

    def test_create_label(self):
        label = Label.objects.create(name="Test Label")
        self.assertEqual(str(label), "Test Label")

    def test_create_labeled_task(self):
        project = Project.objects.create(name="Test Project", workspace=self.workspace)
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            status="todo",
            project=project,
            due_date=timezone.now() + timezone.timedelta(days=7),
        )
        label = Label.objects.create(name="Test Label")
        labeled_task = LabeledTask.objects.create(label=label, task=task)
        self.assertEqual(
            str(labeled_task), "Label 'Test Label' on task 'Test Task'"
        )

