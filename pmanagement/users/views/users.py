"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
    )
from pmanagement.users.permissions import IsAccountOwner

# Serializer
from pmanagement.users.serializers.profiles import ProfileModelSerializer
from pmanagement.projects.serializers import ProjectModelSerializer
from pmanagement.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# Models
from pmanagement.users.models import User
from pmanagement.projects.models import Project


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    """User view set.
    Handle sign up, login and account verification
    """

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permisson based on actions."""
        if self.action in ['signup', 'login']:
            permission = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission = [IsAuthenticated, IsAccountOwner]
        else:
            permission = [IsAuthenticated]

        return [p() for p in permission]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User login. """
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'acces_token': token,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User signup ."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
                      profile,
                      data=request.data,
                      partial=partial
                      )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        """Add extra date to the response. """
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        projects = Project.objects.filter(
                  members=request.user,
                  )
        data = {
              'user': response.data,
              'project': ProjectModelSerializer(projects, many=True).data
              }
        response.data = data
        return response
