from django.core.files.storage import FileSystemStorage
from django.db import models
from .models import Show

fs = FileSystemStorage(location="/tmp/pyhon_media")

from bands.models import Band

class ShowManager(models.Manager):
  def get_by_id(id: int) -> Show:
    return Show.objects.get(id=id)
  def shows_for_band(band: Band) -> models.BaseManager[Show]:
    return Show.objects.filter(band=band).order_by('-starts_at')
