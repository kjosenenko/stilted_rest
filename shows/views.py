from django.http import JsonResponse
from .serializers import ShowSerializer, ShowsSerializer
from .managers import ShowManager
from bands.managers import BandManager

def shows(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      shows = ShowManager.shows_for_band(band)
      serializer = ShowsSerializer(shows, many=True, context={'request': request})
      return JsonResponse(serializer.data, safe=False)
    
def show(request, id):
  if request.method == 'GET':
    show = ShowManager.get_by_id(id)
    if not show:
      return JsonResponse({"error": "Show not found."}, status=404)
    else:
      serializer = ShowSerializer(show, context={'request': request})
      return JsonResponse(serializer.data, safe=False)
