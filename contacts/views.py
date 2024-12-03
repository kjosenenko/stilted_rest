from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bands.models import Band
from .forms import ContactForm

@csrf_exempt
def contact(request):
  if request.method == 'POST':
    try: 
      data = JSONParser().parse(request)
      host = request.headers['X-Forwarded-Host']
      band = Band.objects.get(url=host)
      
      if band.using_react:
        data['data']['band_id'] = band.id
        form = ContactForm(data['data'])
      else:
        data['band_id'] = band.id
        form = ContactForm(data)

      
      if form.is_valid():
        ContactForm.send_email(form)
        return JsonResponse(data, status=202)
      else:
        return JsonResponse(form.errors, status=406)
    except:
      # This is porbably because a band was not found for the host.  Either a band is configured wrong or the origin is suspect.
      JsonResponse("An error occurred.", status=400)

