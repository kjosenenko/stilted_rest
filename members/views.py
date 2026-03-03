from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from bands.models import Band
from .managers import MemberManager
from .serializers import MemberSerializer
from bands.managers import BandManager

@api_view(['GET'])
def members(request: HttpRequest) -> Response:
  band: Band | None = BandManager.find_by_request(request)
  if not band:
    return Response({"error": "Band not found."}, status=status.HTTP_404_NOT_FOUND)
  
  serializer = MemberSerializer(MemberManager.band_members(band), many=True)
  return Response(serializer.data)
