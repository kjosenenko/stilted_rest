from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from bands.models import Band
from .managers import MemberManager
from .serializers import MemberSerializer
from bands.managers import BandManager

@swagger_auto_schema(
    method='get',
    operation_description='Get all members for a band',
    responses={200: MemberSerializer(many=True), 404: 'Band not found'},
    tags=['members']
)
@api_view(['GET'])
def members(request: HttpRequest) -> Response:
  band: Band | None = BandManager.find_by_request(request)
  if not band:
    return Response({"error": "Band not found."}, status=status.HTTP_404_NOT_FOUND)
  
  serializer = MemberSerializer(MemberManager.band_members(band), many=True)
  return Response(serializer.data)
