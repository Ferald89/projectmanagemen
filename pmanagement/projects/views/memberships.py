"""Project membership views."""

# Django REST Framework
from rest_framework import viewsets, status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from pmanagement.projects.models import Project, Membership

# Permissions
from rest_framework.permissions import IsAuthenticated
from pmanagement.projects.permissions.memberships import IsSelfMember

# Serialer
from pmanagement.projects.serializers import MembershipModelSerializer, AddMemberSerializer


class MembershipViewSet(
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = MembershipModelSerializer
    """Project membership view set."""

    def dispatch(self, request, *args, **kwargs):
        """Verify that project exists."""
        slug_name = kwargs['slug_name']
        self.project = get_object_or_404(Project, slug_name=slug_name)
        return super(MembershipViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        """Assign permissions based on actions"""
        permissions = [IsAuthenticated]
        if self.action == 'invitations':
            permissions.append(IsSelfMember)
        return [p() for p in permissions]

    def get_queryset(self):
        """Return Project members."""
        return Membership.objects.filter(
            project=self.project
        )

    def perform_destroy(self, instance):
        """Disable membership."""
        instance.is_active = False
        instance.save()

    def create(self, request, *args, **kwargs):
        """Handle members creation from invitation code."""
        serializer = AddMemberSerializer(
            data=request.data,
            context={'project': self.project, 'request': request}
            )
        serializer.is_valid(raise_exception=True)
        member = serializer.save()

        data = self.get_serializer(member).data
        return Response(data, status=status.HTTP_201_CREATED)
