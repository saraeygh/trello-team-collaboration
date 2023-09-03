from django.db import models

from workspace.models import Workspace
from workspace.validators import validate_file_size

# Mahdieh
class WorkspaceImage(models.Model):
    workspace = models.OneToOneField(
        Workspace,
        on_delete=models.CASCADE,
        related_name='images',
        )
    
    image = models.ImageField(
        upload_to= 'workspace/images',
        validators=[validate_file_size],

    )
