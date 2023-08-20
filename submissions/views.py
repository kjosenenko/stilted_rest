from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import SubmissionSerializer

@csrf_exempt
def submit(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = SubmissionSerializer(data=data['data'])
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
  else:
    return JsonResponse(serializer.errors, status=400)
