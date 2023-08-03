from django.utils.translation import gettext_lazy as _
from django.db import models


# Reza
class ActiveObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(soft_delete=False)


# Reza
class DeactiveObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(soft_delete=True)


# RezaS
class BaseModel(models.Model):

    objects = ActiveObjects()
    archived = DeactiveObjects()

    soft_delete = models.BooleanField(
        default=False,
        verbose_name=_("Soft delete")
        )

    def delete(self):
        self.soft_delete = True
        self.save()

    class Meta:
        abstract = True


# RezaS
class TimeMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True
        )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True
        )

    class Meta:
        abstract = True
