""""Items views."""

# Django REST Frameworks
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from pmanagement.items.serializers import(
                            CreateItemSerializer,
                            ItemModelSerializer
                    )

# Models
from pmanagement.projects.models import Project


class ItemViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """Item view set."""

    def dispatch(self, request, *arg, **kwargs):
        """Verify that the project exists. """
        slug_name = kwargs['slug_name']
        self.project = get_object_or_404(Project, slug_name=slug_name)
        return super(ItemViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        """Assign permission based on action"""
        permissions = [IsAuthenticated]