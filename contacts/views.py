from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from bands.models import Band
from bands.managers import BandManager
from .forms import ContactForm
from .managers import ContactManager
from .serializers import ContactRequestSerializer, ContactResponseSerializer

@swagger_auto_schema(
    method='post',
    operation_description='Submit a contact form for a band',
    request_body=ContactRequestSerializer,
    responses={
        202: ContactResponseSerializer(),
        404: 'Band not found',
        406: 'Invalid form data'
    },
    tags=['contacts']
)
@api_view(['POST'])
def contact(request: HttpRequest) -> Response:
  data = request.data
  band: Band | None = BandManager.find_by_request(request)
  
  if not band:
    # Either a band is not configured with the correct URL or the request is coming from a suspect source.
    return Response({"error": "Band not found."}, status=status.HTTP_404_NOT_FOUND)

  data['band_id'] = band.id
  form = ContactForm(data)
  
  if form.is_valid():
    ContactManager.forward_to_band(form)
    return Response(data, status=status.HTTP_202_ACCEPTED)
  else:
    return Response(form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
