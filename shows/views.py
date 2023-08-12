from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Show
from .serializers import ShowSerializer

def shows(request):
  if request.method == 'GET':
    shows = Show.objects.all()
    serializer = ShowSerializer(shows, many=True)
    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse(serializer.errors, status=400)
