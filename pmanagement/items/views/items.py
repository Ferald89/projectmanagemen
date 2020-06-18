""""Items views."""

# Django REST Frameworks
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from pmanagement.items.serializers import ItemModelSerializer, CreateItemSerializer

# Models
from pmanagement.projects.models import Project


class ItemViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """Item view set."""

    def dispatch(self, request, *args, **kwargs):
        """Verify that the project exists. """
        slug_name = kwargs['slug_name']
        self.project = get_object_or_404(Project, slug_name=slug_name)
        return super(ItemViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        """Assign permission based on action"""
        permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_serializer_context(self):
        """Add project to serializer context"""
        context = super(ItemViewSet, self).get_serializer_context()
        context['project'] = self.project
        return context

    def get_serializer_class(self):
        """Return serializer based on action. """
        if self.action == 'create':
            return CreateItemSerializer
        return ItemModelSerializer

    def get_queryset(self):
        """Return active projec's item."""
        return self.project.item_set.all()
