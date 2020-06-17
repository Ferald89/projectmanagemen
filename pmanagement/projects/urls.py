"""Project URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import projects as projects_views
from .views import memberships as membership_views

router = DefaultRouter()
router.register(r'projects', projects_views.ProjectViewSet, basename='project')
router.register(
        r'projects/(?P<slug_name>[a-zA-Z0-p_-]+)/members',
        membership_views.MembershipViewSet,
        basename='membership'
            )

urlpatterns = [
    path('', include(router.urls))
]
