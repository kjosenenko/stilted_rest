from django.http import HttpRequest
from django.db.models.manager import BaseManager
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from bands.models import Band

from shows.models import Show

from shows.models import Show
from .serializers import ShowSerializer, ShowsSerializer
from .managers import ShowManager
from bands.managers import BandManager

@api_view(['GET'])
def shows(request: HttpRequest) -> Response:
  band: Band | None = BandManager.find_by_request(request)
  if not band:
    return Response({"error": "Band not found."}, status=status.HTTP_404_NOT_FOUND)
  
  shows: BaseManager[Show] = ShowManager().shows_for_band(band)
  serializer = ShowsSerializer(shows, many=True, context={'request': request})
  return Response(serializer.data)
    
@api_view(['GET'])
def show(request: HttpRequest, id: int) -> Response:
  show: Show | None = ShowManager().get_by_id(id)
  if not show:
    return Response({"error": "Show not found."}, status=status.HTTP_404_NOT_FOUND)
  
  serializer = ShowSerializer(show, context={'request': request})
  return Response(serializer.data)
