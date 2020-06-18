"""Item permissions. """

# Django REST Framework
from rest_framework.permisssions import BasePermission


class IsItemOwener(BasePermission):
    """Verify requestin user is the item create."""
    pass
