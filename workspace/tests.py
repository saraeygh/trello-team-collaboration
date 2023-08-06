from django.test import TestCase
from accounts.models import User
from .models import Workspace, Project


# Mahdieh
class WorkspaceModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', 
            password='user1_password'
            )
        
        self.user2 = User.objects.create_user(
            username='user2', 
            password='user2_password'
            )
        
        self.workspace = Workspace.objects.create(
            name='Test Workspace', 
            description='This is a test workspace.'
            )


    def test_create_project(self):
        project = self.workspace.create_project(name='Test Project', description='This is a test project.')
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(project.name, 'Test Project')
        self.assertEqual(project.description, 'This is a test project.')
        self.assertEqual(project.workspace, self.workspace)

    def test_get_members(self):
        self.workspace.add_member(self.user1)
        self.workspace.add_member(
            self.user2, 
            access_level=Workspace.Access.ADMIN
            )
        
        members = self.workspace.get_members()
        self.assertEqual(members.count(), 2)
        self.assertTrue(self.user1 in members)
        self.assertTrue(self.user2 in members)

    def test_remove_member_as_admin(self):
        self.workspace.add_member(self.user1)
        self.workspace.add_member(self.user2, access_level=Workspace.Access.ADMIN)

        self.assertTrue(self.user1 in self.workspace.get_members())
        self.assertTrue(self.user2 in self.workspace.get_members())

        self.workspace.remove_member(self.user1)

        self.assertFalse(self.user1 in self.workspace.get_members())
        self.assertTrue(self.user2 in self.workspace.get_members())

    def test_remove_member_as_non_admin(self):
        self.workspace.add_member(self.user1)

        self.assertTrue(self.user1 in self.workspace.get_members())

        # User1 is not an admin, so they shouldn't be able to remove members
        self.workspace.remove_member(self.user2)

        self.assertTrue(self.user1 in self.workspace.get_members())
        self.assertTrue(self.user2 in self.workspace.get_members())

    def test_modify_access_level_as_admin(self):
        self.workspace.add_member(self.user1)
        self.workspace.add_member(self.user2, access_level=Workspace.Access.ADMIN)

        self.assertEqual(self.workspace.
                         get_members().get(user=self.user1).
                         access_level, Workspace.Access.MEMBER)
        self.assertEqual(self.workspace.
                         get_members().get(user=self.user2).
                         access_level, Workspace.Access.ADMIN)

        self.workspace.modify_access_level(
            self.user1, 
            access_level=Workspace.Access.ADMIN
            )

        self.assertEqual(self.workspace.
                         get_members().get(user=self.user1).
                         access_level, Workspace.Access.ADMIN)
        self.assertEqual(self.workspace.
                         get_members().get(user=self.user2).
                         access_level, Workspace.Access.ADMIN)

    def test_modify_access_level_as_non_admin(self):
        self.workspace.add_member(self.user1)

        self.assertEqual(self.workspace.
                         get_members().get(user=self.user1).
                         access_level, Workspace.Access.MEMBER)

        # User1 is not an admin, so they shouldn't be able to modify access levels
        self.workspace.modify_access_level(
            self.user1, 
            access_level=Workspace.Access.ADMIN)

        self.assertEqual(
            self.workspace.
            get_members().get(user=self.user1).
            access_level, Workspace.Access.MEMBER)


# Mahdieh
class ProjectModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', 
            password='user1_password'
            )
        
        self.user2 = User.objects.create_user(
            username='user2', 
            password='user2_password'
            )
        
        self.workspace = Workspace.objects.create(
            name='Test Workspace', 
            description='This is a test workspace.'
            )
        
        self.project = self.workspace.create_project(
            name='Test Project', 
            description='This is a test project.'
            )

    def test_create_card(self):
        card = self.project.create_card(
            title='Test Card', 
            description='This is a test card.'
            )
        
        self.assertEqual(
            self.project.get_cards().count(), 1)
        self.assertEqual(
            card.title, 'Test Card')
        self.assertEqual(
            card.description, 'This is a test card.')
        self.assertEqual(
            card.list.project, self.project)

