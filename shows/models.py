from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.timezone import localdate
from bands.models import Band
import os

fs = FileSystemStorage(location="/tmp/pyhon_media")

class Show(models.Model):
  venue = models.CharField(max_length=128, blank=True, null=True)
  presale_link = models.CharField(max_length=128, blank=True, null=True)
  has_presale = models.BooleanField(default=False)
  show_date_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to="shows", null=True, blank=True)
  band = models.ForeignKey(Band, on_delete=models.CASCADE)
  
  def current_shows():
    today = localdate()
    return Show.objects.filter(show_date_time__gte=today).extra(order_by=['show_date_time']).reverse()
    
  def past_shows():
    today = localdate()
    return Show.objects.filter(show_date_time__lt=today).extra(order_by=['show_date_time']).reverse()
  
  def cleanup():
    shows = Show.past_shows().exclude(image='')
    for show in shows:
      os.remove(show.image.path)
      show.image=''
      show.save()
    
