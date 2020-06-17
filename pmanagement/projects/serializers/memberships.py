"""Membership serializer."""

# Django REST Framework
from rest_framework import serializers

# Serializer
from pmanagement.users.serializers import UserModelSerializer

# Models
from pmanagement.projects.models import Membership


class MembershipModelSerializer(serializers.ModelSerializer):
    """Member model serializer."""

    user = UserModelSerializer(read_only=True)

    class Meta:
        model = Membership
        fields = (
            'user',
            'is_admin',
            )
        read_only_fields = (
            'user'
            )


class AddMemberSerializer(serializers.Serializer):
    """Add member serializer.
    Handle the addition of a new member to a project
    Project objects must be provides in the context
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_user(self, data):
        """Verify user isn't already a member."""
        project = self.context['project']
        user = data
        q = Membership.objects.filter(project=project, user=user)
        if q.exists():
            raise serializers.ValidationError('User is already member of this circle')

    def create(self, data):
        """Create new project member. """
        project = self.context['project']
        user = self.context['request'].user

        # Member creation
        member = Membership.objects.create(
                                    user=user,
                                    profile=user.profile,
                                    project=project
        )

        return member
