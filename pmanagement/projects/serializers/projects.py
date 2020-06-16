""""Projects serializer."""

# Django REST FrameWork
from rest_framework import serializers

# Model
from pmanagement.projects.models import Project


class ProjectModelSerializer(serializers.ModelSerializer):
    """Serializer model serializer."""

    class Meta:
        """MEta class."""
        model = Project
        fields = (
            'name',
            'slug_name',
            'about',
            'picture',
            'budget',
            'client',
            'percentage',
            'manager',
            'started_date',
            'delivery_date'
        )

    def validate(self, data):
        return data
