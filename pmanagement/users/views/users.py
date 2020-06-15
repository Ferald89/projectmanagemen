"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    """User view set.
    Handle sign up, login and account verification
    """

    queryset = User.objects.all()
