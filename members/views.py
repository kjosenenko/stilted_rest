from django.http import JsonResponse
from .managers import MemberManager
from .serializers import MemberSerializer
from bands.managers import BandManager

def members(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = MemberSerializer(MemberManager.band_members(band), many=True)
      return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse(serializer.errors, status=400)
