from django.core.files.storage import FileSystemStorage
from django.db import models
from .models import Music


class MusicManager(models.Manager):
  
  def music_for_band(band):
    return Music.objects.filter(band=band)