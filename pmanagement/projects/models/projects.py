"""projects model."""

# Django
from django.db import models

# Utilities
from pmanagement.utils.models import PManagementModel


class Project(PManagementModel):
    """Project model."""

    name = models.CharField('project name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)
    about = models.CharField('project description', max_length=255)
    picture = models.ImageField(upload_to='project/picture', blank=True, null=True)

    budget = models.DecimalField(default=0, max_digits=999, decimal_places=4)

    client = models.CharField('client', max_length=140)

    percentage = models.PositiveIntegerField(default=0)

    manager = models.ForeignKey(
                'users.User',
                on_delete=models.SET_NULL,
                null=True
        )

    started_date = models.DateTimeField()
    delivery_date = models.DateTimeField()

    def __str__(self):
        """Return project name."""
        return self.name
