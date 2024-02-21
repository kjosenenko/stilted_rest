from django.core.files.storage import FileSystemStorage
from django.db import models
from django.core.cache import cache
from django.utils.timezone import localdate

fs = FileSystemStorage(location="/tmp/pyhon_media")

class Show(models.Model):
  venue = models.CharField(max_length=128, blank=True, null=True)
  presale_link = models.CharField(max_length=128, blank=True, null=True)
  has_presale = models.BooleanField(default=False)
  show_date_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to="shows", null=True)
  
  def current_shows():
    today = localdate()
    return Show.objects.filter(show_date_time__gte=today).extra(order_by=['show_date_time']).reverse()
    
  def past_shows():
    today = localdate()
    return Show.objects.filter(show_date_time__lt=today).extra(order_by=['show_date_time']).reverse()
  
  def cleanup():
    t = 2419200
    if cache.get('recently_run') == 'true':
      return
    else:
      cache.set('recently_run', 'true', 10)
      have_images = Show.past_shows().exclude(image='')
      breakpoint()
    
