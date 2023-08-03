from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, TimeMixin


# RezaS
class User(AbstractUser, BaseModel):
    pass


# RezaS
class UserProfile(TimeMixin, BaseModel):

    GENDER_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
    }

    birthdate = models.DateField(
        verbose_name=_("Birthdate"),
        help_text=_("Insert your birthday (Optional)"),
        blank=True,
        null=True
        )

    phone = models.CharField(
        verbose_name=_("Phone number"),
        help_text=_("Insert your phone number (Optional)"),
        max_length=11,
        blank=True,
        null=True
        )

    gender = models.CharField(
        verbose_name=_("Gender"),
        help_text=_("Select your gender"),
        choices=GENDER_CHOICES,
        max_length=10
        )
