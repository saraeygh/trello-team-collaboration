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


#Mahdieh
class Board(models.Model):
    owner_model = models.ForeignKey(
        ContentType,
        blank=False,
        null=False,
        related_name='board',
        on_delete=models.CASCADE,
        limit_choices_to=models.Q(app_label='users', model='user') | models.Q(app_label='projects', model='project')
    )
    owner = GenericForeignKey(
        'owner_model',
        'owner_id'
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    description = models.TextField(
        blank=True,
        null=True)
    # image = models.ImageField(
    #     blank=True,
    #     null=True,
    #     upload_to='board_images'
    # )
    color = models.CharField(
        blank=True,
        null=False,
        max_length=6
    )