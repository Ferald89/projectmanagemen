"""Items URLs. """

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import items as items_views

router = DefaultRouter()
router.register(
            r'circles/(?P<slug_name>[a-zA-Z0-p_-]+)/items',
            items_views.ItemViewSet,
            basename='items'
            )

urlpatterns = [
            path('', include(router.urls))
            ]
