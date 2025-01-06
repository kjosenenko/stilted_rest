from django.http import JsonResponse
from .managers import MusicManager
from .serializers import MusicSerializer
from bands.managers import BandManager

def music(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = MusicSerializer(MusicManager.music_for_band(band), many=True)
      return JsonResponse(serializer.data, safe=False)
