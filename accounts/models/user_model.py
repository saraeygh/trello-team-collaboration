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

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def phone(self):
        return self.profile.phone

    def gender(self):
        return self.profile.gender

    def birthdate(self):
        return self.profile.birthdate
