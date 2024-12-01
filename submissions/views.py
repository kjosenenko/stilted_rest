from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bands.models import Band
from .forms import Submission

@csrf_exempt
def submit(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    host = request.headers['X-Forwarded-Host']
    band_id = Band.objects.get(url=host).id
    data['data']['band_id'] = band_id
    
    # Comment in for React client.
    form = Submission(data['data'])

    # Comment in for Vue client.
    # form = Submission(data)

    
    if form.is_valid():
      Submission.send_email(form)
      return JsonResponse(data, status=201)
    else:
      return JsonResponse(form.errors, status=400)
