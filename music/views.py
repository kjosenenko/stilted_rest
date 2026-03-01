from django.http import HttpRequest
from django.db.models.manager import BaseManager
from django.http import JsonResponse

from bands.models import Band

from music.models import Music
from .managers import MusicManager
from .serializers import MusicSerializer
from bands.managers import BandManager
import logging

logger: logging.Logger = logging.getLogger(__name__)

def music(request: HttpRequest) -> JsonResponse | None:
  if request.method == 'GET':
    band: Band | None = BandManager.find_by_request(request)
    if not band:
      logger.error("Band not found for request")
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      music_list: BaseManager[Music] = MusicManager.music_for_band(band)
      logger.info(f"Found {music_list.count()} music items for band {band.name}")
      serializer = MusicSerializer(music_list, many=True)
      return JsonResponse(serializer.data, safe=False)

  return None
