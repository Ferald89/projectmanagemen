"""Project URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import projects as projects_views

router = DefaultRouter()
router.register(r'projects', projects_views.ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls))
]
