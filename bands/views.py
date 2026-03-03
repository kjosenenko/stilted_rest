from django.db.models.manager import BaseManager
from django.http import HttpRequest
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BandSerializer
from .models import Band
from .managers import BandManager

@api_view(['GET'])
def band(request: HttpRequest) -> Response:
  band: Band | None = BandManager.find_by_request(request)
  if not band:
    return Response({"error": "Band not found."}, status=status.HTTP_404_NOT_FOUND)
  
  serializer = BandSerializer(band, context={'request': request})
  return Response(serializer.data)

class BandViewSet(viewsets.ModelViewSet):
    queryset: BaseManager[Band] = Band.objects.all()
    serializer_class = BandSerializer

      # If you have custom methods, add type hints for their arguments as well
