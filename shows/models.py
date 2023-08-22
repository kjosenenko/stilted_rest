from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location="/tmp/pyhon_media")

class Show(models.Model):
  venue = models.CharField(max_length=128, blank=True, null=True)
  presale_link = models.CharField(max_length=128, blank=True, null=True)
  has_presale = models.BooleanField(default=False)
  supporting_acts = models.TextField(blank=True, null=True)
  show_date_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(storage=fs, null=True)
