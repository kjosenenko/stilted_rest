from django.http import HttpRequest
from django.http import JsonResponse

from bands.models import Band
from .managers import MemberManager
from .serializers import MemberSerializer
from bands.managers import BandManager

def members(request: HttpRequest) -> JsonResponse:
  if request.method == 'GET':
    band: Band | None = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = MemberSerializer(MemberManager.band_members(band), many=True)
      return JsonResponse(serializer.data, safe=False)
  return JsonResponse({"error": "Invalid request method."}, status=400)
