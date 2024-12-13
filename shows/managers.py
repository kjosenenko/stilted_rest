from django.core.files.storage import FileSystemStorage
from django.db import models
from .models import Show
from django.utils.timezone import localdate
import os

fs = FileSystemStorage(location="/tmp/pyhon_media")

class ShowManager(models.Manager):
  
  def current_shows_for_band(band):
    today = localdate()
    return Show.objects.filter(band=band).filter(show_date_time__gte=today).extra(order_by=['show_date_time']).reverse()
    
  def past_shows_for_band(band):
    today = localdate()
    return Show.objects.filter(band=band).filter(show_date_time__lt=today).extra(order_by=['show_date_time']).reverse()
  
  def cleanup():
    shows = Show.past_shows().exclude(image='')
    for show in shows:
      os.remove(show.image.path)
      show.image=''
      show.save()
    
