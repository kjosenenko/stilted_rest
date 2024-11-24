from django.db import models
from django.core.files.storage import FileSystemStorage
from django_cryptography.fields import encrypt

fs = FileSystemStorage(location="/tmp/pyhon_media")

class Band(models.Model):
  name = models.CharField(max_length=128, blank=True, null=True, unique=True)
  url = models.CharField(max_length=128, blank=True, null=True, unique=True)
  email = models.CharField(max_length=128, blank=True, null=True, unique=True)
  email_password = encrypt(models.CharField(max_length=128, blank=True, null=True))
  smtp_server = models.CharField(max_length=128, blank=True, null=True)
  smtp_port = models.IntegerField(blank=True, null=True)
  bio = models.TextField(blank=True)
  cover_photo = models.ImageField(upload_to="bands", null=True, blank=True)
  logo = models.ImageField(upload_to="bands", null=True, blank=True)
  using_react = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)