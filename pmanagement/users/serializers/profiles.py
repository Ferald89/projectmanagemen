"""Profile serializer. """

# Django REST Framework
from rest_framework import serializers

# Models
from pmanagement.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile Model Serializer. """

    class Meta:
        """Meta Class."""
        model = Profile

        fields = (
                'picture',
                )
