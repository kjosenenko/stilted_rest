from django.db import models
from .models import Band

class BandManager(models.Manager):
  
  @staticmethod
  def find_by_request(request):
    try:
      host = request.headers['X-Forwarded-Host']
    except:
      host = request.headers['Origin']
    try:
      band = Band.objects.get(url=host)
      return band
    except:
      return None