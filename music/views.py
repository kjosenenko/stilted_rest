from django.http import JsonResponse
from .managers import MusicManager
from .serializers import MusicSerializer
from bands.managers import BandManager
import logging

logger = logging.getLogger(__name__)

def music(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      logger.error("Band not found for request")
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      music_list = MusicManager.music_for_band(band)
      logger.info(f"Found {music_list.count()} music items for band {band.name}")
      serializer = MusicSerializer(music_list, many=True)
      return JsonResponse(serializer.data, safe=False)
