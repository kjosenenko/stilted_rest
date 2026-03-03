from django.http import HttpRequest
from django.db.models.manager import BaseManager
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from bands.models import Band

from music.models import Music
from .managers import MusicManager
from .serializers import MusicSerializer
from bands.managers import BandManager
import logging

logger: logging.Logger = logging.getLogger(__name__)

@api_view(['GET'])
def music(request: HttpRequest) -> Response:
  band: Band | None = BandManager.find_by_request(request)
  if not band:
    logger.error("Band not found for request")
    return Response({"error": "Band not found."}, status=status.HTTP_404_NOT_FOUND)
  
  music_list: BaseManager[Music] = MusicManager.music_for_band(band)
  logger.info(f"Found {music_list.count()} music items for band {band.name}")
  serializer = MusicSerializer(music_list, many=True)
  return Response(serializer.data)
