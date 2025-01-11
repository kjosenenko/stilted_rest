from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bands.managers import BandManager
from .forms import ContactForm
from .managers import ContactManager

@csrf_exempt
def contact(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    band = BandManager.find_by_request(request)
    
    if not band:
      # Either a band is not configured with the correct URL or the request is coming from a suspect source.
      return JsonResponse({"error": "Band not found."}, status=404)

    data['band_id'] = band.id
    form = ContactForm(data)
    
    if form.is_valid():
      ContactManager.forward_to_band(form)
      return JsonResponse(data, status=202)
    else:
      return JsonResponse(form.errors, status=406)
