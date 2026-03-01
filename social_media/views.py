from django.http import HttpRequest
from django.http import JsonResponse

from bands.models import Band
from .managers import SocialMediaManager
from .serializers import SocialMediaSerializer
from bands.managers import BandManager

def social_media(request: HttpRequest) -> JsonResponse | None:
  if request.method == 'GET':
    band: Band | None = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = SocialMediaSerializer(SocialMediaManager.social_media_for_band(band), many=True)
      return JsonResponse(serializer.data, safe=False)

  return None
