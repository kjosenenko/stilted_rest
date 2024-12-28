from django.db import models
from .models import Band

class BandManager(models.Manager):
  
  @staticmethod
  def find_by_request(request):
    try:
      # This would be from the react app.
      host = request.headers['X-Forwarded-Host']
    except:
      # This would be from a vue app.
      host = request.headers['Origin']
    try:
      band = Band.objects.get(url=host)
      return band
    except:
      return None
  
  # change this to a filter (for user) based on the many bands a user can be associated with
  @staticmethod
  def find_by_name(name):
    try:
      band = Band.objects.get(name=name)
      return band
    except:
      return None
    