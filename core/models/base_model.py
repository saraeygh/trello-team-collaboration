from django.utils.translation import gettext_lazy as _
from django.db import models


# RezaS
class BaseModel(models.Model):

    soft_delete = models.BooleanField(
        default=False,
        verbose_name=_("Soft delete")
        )

    def delete(self, *args, **kwargs):
        self.soft_delete = True
        self.save()

    class Meta:
        abstract = True
