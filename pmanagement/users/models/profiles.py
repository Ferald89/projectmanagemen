"""Profile model."""

# Django
from django.db import models

# Utilities
from pmanagement.utils.models import PManagementModel


class Profile(PManagementModel):
    """Profile model.
    A profile hold a user's public data like picture,
    an statics.
    """

    user = models.OneToOneField('user.User', on_delete=models.CASCADE)

    picture = models.ImageField(
                'Profile picture',
                upload_to='users/picture/',
                blank=True,
                null=True
    )

    def __str__(self):
        """Return user's"""
        return str(self.user)
