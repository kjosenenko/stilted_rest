from django.db import models
from bands.models import Band

class Contact(models.Model):
  name = models.CharField(max_length=128, blank=True, null=True)
  email = models.CharField(max_length=128, blank=True, null=True)
  phone = models.CharField(max_length=128, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  band = models.ForeignKey(Band, on_delete=models.CASCADE)
