from __future__ import annotations

from django.core.files.storage import FileSystemStorage
from django.db import models
from .models import SocialMedia


from bands.models import Band

class SocialMediaManager(models.Manager):
  def social_media_for_band(band: Band) -> models.QuerySet[SocialMedia]:
    return SocialMedia.objects.filter(band=band)