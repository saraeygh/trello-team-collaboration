from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register("users", views.CustomeUserViewSet)

urlpatterns = router.urls
