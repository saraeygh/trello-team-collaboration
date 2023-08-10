from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
# router.register('workspaces', views.WorkspaceViewSet, basename='workspaces')
router.register('labels', views.LabelViewSet, basename='labels')


# workspaces_router = routers.NestedDefaultRouter(
#     router, 'workspaces', lookup='workspace'
#     )
# workspaces_router.register(
#     'projects', views.ProjectViewSet, basename='workspace-projects'
#     )
# workspaces_router.register(
#     'workspacemembers', views.WorkspaceMemberViewSet, basename='workspace-members'
#     )

# projects_router = routers.NestedDefaultRouter(
#     workspaces_router, 'projects', lookup='project'
#     )
# projects_router.register(
#     'members', views.ProjectMemeberViewSet, basename='project-memebrs'
#     )
# projects_router.register(
#     'tasks', views.TaskViewSet, basename='project-tasks'
#     )

# tasks_router = routers.NestedDefaultRouter(
#     projects_router, 'tasks', lookup='task'
#     )
# tasks_router.register(
#     'assignments', views.AssignmentViewSet, basename='tasks-assignments'
#     )
# tasks_router.register(
#     'comments', views.CommentViewSet, basename='tasks-comments'
#     )

urlpatterns = (
    router.urls
    # + workspaces_router.urls
    # + projects_router.urls
    # + tasks_router.urls
    )
