from django.http import JsonResponse
from .serializers import BandSerializer, BandImagesSerializer
from .managers import BandManager

def band(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = BandSerializer(band)
      return JsonResponse(serializer.data, safe=False)
    
def images(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = BandImagesSerializer(band)
      return JsonResponse(serializer.data, safe=False)
