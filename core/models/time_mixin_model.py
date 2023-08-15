from django.utils.translation import gettext_lazy as _
from django.db import models


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
