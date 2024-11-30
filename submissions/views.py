from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bands.models import Band

@csrf_exempt
def submit(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    host = request.headers['X-Forwarded-Host']
    band_id = Band.objects.get(url=host).id
    # data['data']['band_id'] = band_id
    breakpoint()
    
    # Comment in for React client.
    # serializer = SubmissionSerializer(data=data['data'])

    # Comment in for Vue client.
    # serializer = SubmissionSerializer(data=data)
    return JsonResponse(data, status=201)

    
  #   if serializer.is_valid():
  #     serializer.save()
  #     return JsonResponse(serializer.data, status=201)
  #   return JsonResponse(serializer.errors, status=400)
  # else:
  #   return JsonResponse(serializer.errors, status=400)
