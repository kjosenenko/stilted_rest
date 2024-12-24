from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

fs = FileSystemStorage(location="/tmp/pyhon_media")

class Image(models.Model):
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey()
  image = models.ImageField(upload_to="images", null=True, blank=True)
  alt = models.CharField(max_length=128, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.alt
