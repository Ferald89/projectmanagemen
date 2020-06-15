"""User Models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from pmanagement.utils.models import PManagementModel


class User(PManagementModel, AbstractUser):
    """User mode.
    Extend from django's Abstact User,Change the username field
    to email and add some extra fields
    """
    email = models.EmailField(
        'email dress',
        unique=True,
        error_messages={
                        'unique': 'A USer with that email already exist.'
        }
    )

    phone_regex = RegexValidator(
         regex=r'\+?1?\d{9,15}$',
         message="Phone number must be entered in the format: +9999999. up to 15 digits allowed."
         )

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def ___str__(self):
        return self.email

    def get_short_name(self):
        return self.email
