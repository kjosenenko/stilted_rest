from __future__ import annotations

from django.core.files.storage import FileSystemStorage
from django.db import models
from .models import Show
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Show

fs = FileSystemStorage(location="/tmp/pyhon_media")

from bands.models import Band

class ShowManager(models.Manager):
  def get_by_id(self, id: int) -> Show | None:
    try:
      show: Show = Show.objects.get(id=id)
      return show
    except Show.DoesNotExist:
      return None
  
  def shows_for_band(self, band: Band) -> models.QuerySet[Show]:
    return Show.objects.filter(band=band).order_by('-starts_at')
