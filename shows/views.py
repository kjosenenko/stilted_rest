from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .managers import ShowManager
from .serializers import ShowSerializer
from bands.managers import BandManager

def shows(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = ShowSerializer(ShowManager.shows_for_band(band), many=True)
      return JsonResponse(serializer.data, safe=False)
