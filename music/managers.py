from __future__ import annotations

from django.core.files.storage import FileSystemStorage
from django.db import models
from .models import Music


from bands.models import Band

class MusicManager(models.Manager):
  def music_for_band(band: Band) -> models.QuerySet[Music]:
    return Music.objects.filter(band=band)