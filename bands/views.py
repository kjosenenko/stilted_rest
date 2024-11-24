from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import BandSerializer
from .models import Band

def band(request):
  if request.method == 'GET':
    host = request.headers['X-Forwarded-Host']
    serializer = BandSerializer(Band.objects.get(url=host))
    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse(serializer.errors, status=400)