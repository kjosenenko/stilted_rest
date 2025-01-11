from django.db import models
from .models import Band

class BandManager(models.Manager):
  
  @staticmethod
  def find_by_request(request):
    try:
      # Get Origin header which is automatically set by browser
      origin = request.headers.get('Origin', '')
      if origin:
        return Band.objects.get(url=origin)
      
      # Fallback to host if no Origin (e.g., direct browser request)
      host = request.get_host()
      if 'localhost' in host:
        return Band.objects.get(url='http://localhost:5173')
      return Band.objects.get(url=f'https://{host}')
      
    except Band.DoesNotExist:
      return None
