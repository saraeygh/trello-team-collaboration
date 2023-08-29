from rest_framework_nested import routers

from .views import (
    WorkspaceViewSet,
    LabeledTaskViewSet,
    WorkspaceMemberViewSet,
    ProjectViewSet,
    WorkspaceProjectViewSet,
    ProjectMemberViewSet,
    TaskViewSet,
    TaskViewSetNone,
    AssignmentViewSet,
    CommentViewSet,
    )

router = routers.DefaultRouter()
router.register('workspaces', WorkspaceViewSet, basename='workspaces')
router.register('projects', ProjectViewSet, basename='projects')
router.register('tasks', TaskViewSetNone, basename='tasks')

workspaces_router = routers.NestedDefaultRouter(router, 'workspaces', lookup='workspace')
workspaces_router.register('projects', WorkspaceProjectViewSet, basename='workspace-projects')
workspaces_router.register('members', WorkspaceMemberViewSet, basename='workspace-members')

projects_router = routers.NestedDefaultRouter(router, 'projects', lookup='project')
projects_router.register('members', ProjectMemberViewSet, basename='project-memebrs')
projects_router.register('tasks', TaskViewSet, basename='project-tasks')

tasks_router = routers.NestedDefaultRouter(router, 'tasks', lookup='task')
tasks_router.register('assignments', AssignmentViewSet, basename='tasks-assignments')
tasks_router.register('comments', CommentViewSet, basename='tasks-comments')
tasks_router.register('labels', LabeledTaskViewSet, basename='tasks-labels')

urlpatterns = (
    router.urls
    + workspaces_router.urls
    + projects_router.urls
    + tasks_router.urls
    )
