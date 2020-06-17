"""Project memberships classes. """

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsSelfMember(BasePermission):
    """Allow acces only to member owner."""

    def has_permission(self, request, view):
        """Let object permission gran acess. """
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Allow acces only if member is owned by the requesting user."""
        return request.user == obj.user
