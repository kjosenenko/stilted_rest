from django.db import models
from .models import Band

class BandManager(models.Manager):
  
  @staticmethod
  def find_by_request(request):
    
    # Comment in below to test in browser, you'll need to create a band named "Stilted" first
    # band = Band.objects.get(name='Stilted')
    # return band
    
    # Comment out below to test in browser
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
