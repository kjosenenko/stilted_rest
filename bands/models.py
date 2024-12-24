from django.db import models
from django_cryptography.fields import encrypt
from images.models import Image
from django.contrib.contenttypes.fields import GenericRelation

class Band(models.Model):
  name = models.CharField(max_length=128, blank=True, null=True, unique=True)
  url = models.CharField(max_length=128, blank=True, null=True, unique=True)
  email = models.CharField(max_length=128, blank=True, null=True, unique=True)
  email_password = encrypt(models.CharField(max_length=128, blank=True, null=True))
  smtp_server = models.CharField(max_length=128, blank=True, null=True)
  smtp_port = models.IntegerField(blank=True, null=True)
  bio = models.TextField(blank=True)
  cover_photo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, default=None, related_name="cover_photos")
  logo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, default=None, related_name="logos")
  images = GenericRelation(Image)
  using_react = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
