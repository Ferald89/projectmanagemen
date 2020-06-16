"""Projects views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Permissions
from rest_framework.permissions import IsAuthenticated
from pmanagement.projects.permissions.projects import IsProjectAdmin

# Serializer
from pmanagement.projects.serializers import ProjectModelSerializer

# Model
from pmanagement.projects.models import Project, Membership


class ProjectViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Project view set."""
    serializer_class = ProjectModelSerializer
    lookup_field = 'slug_name'

    def get_queryset(self):
        """Restric list to public only"""
        queryset = Project.objects.all()
        if self.action == 'list':
            # chenge to is public project
            return queryset
        return queryset

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permissions.append(IsProjectAdmin)
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        """Assign project admin"""
        project = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            project=project,
            is_admin=True,
        )
