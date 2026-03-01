from django.core.files.storage import FileSystemStorage
from django.db import models
from .models import SocialMedia


class SocialMediaManager(models.Manager):
  
  def social_media_for_band(band: Band) -> models.BaseManager[SocialMedia]:
    return SocialMedia.objects.filter(band=band)