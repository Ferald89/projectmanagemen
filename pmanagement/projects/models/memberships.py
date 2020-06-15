"""Membership model."""

# Django
from django.db import models

# Utilities
from pmanagement.utils.models import PManagementModel


class Membership(PManagementModel):
    """PManagement model.
    A membership is the table  that holds the relationship between
    a user and a project
    """

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)

    is_admin = models.BooleanField(
        'project admin',
        default=False,
        help_text="Project admin can update the projects's data and manage its members."
        )

    def __str__(self):
        """Return username and cirlce."""
        return '@{} at #{}'.format(
                            self.user.username,
                            self.project.slug_name
                            )
