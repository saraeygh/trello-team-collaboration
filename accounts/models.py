from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


# Reza
class User(BaseModel, AbstractUser):
    email = models.EmailField(
        verbose_name=_("email address"),
        help_text=_("Required."),
        unique=True,
        )

    first_name = models.CharField(
        verbose_name=_("first name"),
        help_text=_("Required."),
        max_length=150,
        )

    last_name = models.CharField(
        verbose_name=_("last name"),
        help_text=_("Required."),
        max_length=150,
        )

    GENDER_CHOICES = {
        ('m', 'Male'),
        ('f', 'Female'),
    }

    gender = models.CharField(
        verbose_name=_("Gender"),
        help_text=_("Select your gender"),
        choices=GENDER_CHOICES,
        max_length=1,
        blank=True,
        null=True,
        )

    birthdate = models.DateField(
        verbose_name=_("Birthdate"),
        help_text=_("Insert your birthday (Optional)"),
        blank=True,
        null=True,
        )

    phone = models.CharField(
        verbose_name=_("Phone number"),
        help_text=_("Insert your phone number (Optional)"),
        max_length=11,
        blank=True,
        null=True,
        )
