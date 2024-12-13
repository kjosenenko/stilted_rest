from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import BandSerializer
from .managers import BandManager

def band(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = BandSerializer(band)
      return JsonResponse(serializer.data, safe=False)
