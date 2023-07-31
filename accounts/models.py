from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, TimeMixin


# RezaS
class User(AbstractUser):
    pass


# RezaS
class UserProfile(TimeMixin, BaseModel):

    birthdate = models.DateField(
        verbose_name=_("Birthdate"),
        blank=True,
        null=True
        )

    phone = models.CharField(
        verbose_name=_("Phone number"),
        max_length=11,
        blank=True,
        null=True
        )
