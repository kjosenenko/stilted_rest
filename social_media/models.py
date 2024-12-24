from django.db import models
from bands.models import Band

class SocialMedia(models.Model):
  provider = models.CharField(max_length=128, blank=True, null=True)
  href = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  band = models.ForeignKey(Band, on_delete=models.CASCADE)

  def __str__(self):
    return self.provider
