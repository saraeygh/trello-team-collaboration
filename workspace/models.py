from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from accounts.models import User
from core.models import TimeMixin


# Mahdieh
class Workspace(models.Model, TimeMixin):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )


