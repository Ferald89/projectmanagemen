"""Items model. """

# Django
from django.db import models

# Utilities
from pmanagement.utils.models import PManagementModel


class Item(PManagementModel):
    "Items models"
    name = models.CharField('item name', max_length=140)

    comments = models.TextField(blank=True)

    picture = models.ImageField(upload_to='Item/picture', blank=True, null=True)

    supplier = models.CharField(max_length=140)

    cost = models.DecimalField(default=0, max_digits=999, decimal_places=4)

    current_location = models.CharField(max_length=255)
