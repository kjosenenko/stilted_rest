from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.timezone import localdate
from .models import Show
from .serializers import ShowSerializer

def shows(request):
  if request.method == 'GET':
    today = localdate()
    shows = Show.objects.filter(show_date_time__gte=today).extra(order_by=['show_date_time']).reverse()
    serializer = ShowSerializer(shows, many=True)
    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse(serializer.errors, status=400)

def past_shows(request):
  if request.method == 'GET':
    today = localdate()
    shows = Show.objects.filter(show_date_time__lte=today).extra(order_by=['show_date_time']).reverse()
    serializer = ShowSerializer(shows, many=True)
    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse(serializer.errors, status=400)
