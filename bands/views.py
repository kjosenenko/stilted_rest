from django.db.models.manager import BaseManager
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import BandSerializer
from .models import Band
from .managers import BandManager

from django.http import HttpRequest

def band(request: HttpRequest) -> JsonResponse | None:
  if request.method == 'GET':
    band: Band | None = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = BandSerializer(band, context={'request': request})
      return JsonResponse(serializer.data, safe=False)

  return None

class BandViewSet(viewsets.ModelViewSet):
    queryset: BaseManager[Band] = Band.objects.all()
    serializer_class = BandSerializer

      # If you have custom methods, add type hints for their arguments as well
