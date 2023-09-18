from doctest import BLANKLINE_MARKER
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, TimeMixin
from . import User


# Reza
class Profile(TimeMixin, BaseModel):

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

    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="profile/images",
        blank=True,
        null=True
        )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
        )
