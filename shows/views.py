from django.http import HttpRequest
from django.db.models.manager import BaseManager
from django.http import JsonResponse

from bands.models import Band

from shows.models import Show

from shows.models import Show
from .serializers import ShowSerializer, ShowsSerializer
from .managers import ShowManager
from bands.managers import BandManager

def shows(request: HttpRequest) -> JsonResponse | None:
  if request.method == 'GET':
    band: Band | None = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      shows: BaseManager[Show] = ShowManager.shows_for_band(band)
      serializer = ShowsSerializer(shows, many=True, context={'request': request})
      return JsonResponse(serializer.data, safe=False)
    
def show(request: HttpRequest, id: int) -> JsonResponse | None:
  if request.method == 'GET':
    show: Show = ShowManager.get_by_id(id)
    if not show:
      return JsonResponse({"error": "Show not found."}, status=404)
    else:
      serializer = ShowSerializer(show, context={'request': request})
      return JsonResponse(serializer.data, safe=False)
