from django.core.files.storage import FileSystemStorage
from django.db import models
from .models import Show

fs = FileSystemStorage(location="/tmp/pyhon_media")

class ShowManager(models.Manager):
  
  def shows_for_band(band):
    return Show.objects.filter(band=band).extra(order_by=['show_date_time']).reverse()
