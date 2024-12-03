from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .managers import ShowManager
from .serializers import ShowSerializer

def shows(request):
  if request.method == 'GET':
    serializer = ShowSerializer(ShowManager.current_shows(), many=True)
    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse(serializer.errors, status=400)

def past_shows(request):
  if request.method == 'GET':
    serializer = ShowSerializer(ShowManager.past_shows(), many=True)
    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse(serializer.errors, status=400)
