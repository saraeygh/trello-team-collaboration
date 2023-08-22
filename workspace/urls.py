from rest_framework_nested import routers
from .views import (WorkspaceViewSet,
                    LabelViewSet,
                    LabledTaskViewSet,
                    ProjectViewSet,
                    ProjectMemeberViewSet,
                    TaskViewSet,
                    AssignmentViewSet,
                    CommentViewSet,
                    )

router = routers.DefaultRouter()
router.register('workspaces', WorkspaceViewSet, basename='workspaces')
router.register('projects', ProjectViewSet, basename='projects')
router.register('tasks', TaskViewSet, basename='tasks')
router.register('labels', LabelViewSet, basename='labels')

workspaces_router = routers.NestedDefaultRouter(
     router, 'workspaces', lookup='workspace'
     )
workspaces_router.register(
     'projects', ProjectViewSet, basename='workspace-projects'
     )

projects_router = routers.NestedDefaultRouter(
    router, 'projects', lookup='project'
    )
projects_router.register(
     'members', ProjectMemeberViewSet, basename='project-memebrs'
     )
projects_router.register(
     'tasks', TaskViewSet, basename='project-tasks'
     )

tasks_router = routers.NestedDefaultRouter(
    router, 'tasks', lookup='task'
    )
tasks_router.register(
    'assignments', AssignmentViewSet, basename='tasks-assignments'
    )
tasks_router.register(
    'comments', CommentViewSet, basename='tasks-comments'
    )

labels_router = routers.NestedDefaultRouter(
    router, 'labels', lookup='label'
    )
labels_router.register(
    'labeled-task', LabledTaskViewSet, basename='label-tasks'
    )

urlpatterns = (
    router.urls
    + workspaces_router.urls
    + projects_router.urls
    + tasks_router.urls
    + labels_router.urls
    )
