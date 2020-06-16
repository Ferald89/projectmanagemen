"""Project permissions classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from pmanagement.projects.models import Membership


class IsProjectAdmin(BasePermission):
    """Allow acess. only to project admins."""

    def has_object_permission(self, request, view, obj):
        """Verify user a membership in the obj."""

        try:
            Membership.objects.get(
                user=request.user,
                project=obj
            )
        except Membership.DoesNotExist:
            return False
        return True
