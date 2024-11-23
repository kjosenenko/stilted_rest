from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="/tmp/pyhon_media")

class Band(models.Model):
  band_name = models.CharField(max_length=128, blank=True, null=True, unique=True)
  band_url = models.CharField(max_length=128, blank=True, null=True, unique=True)
  contact_email = models.CharField(max_length=128, blank=True, null=True, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  bio = models.TextField(blank=True)
  cover_photo = models.ImageField(upload_to="bands", null=True)