from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import BandSerializer
from .models import Band
from .managers import BandManager

def band(request):
  if request.method == 'GET':
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = BandSerializer(band, context={'request': request})
      return JsonResponse(serializer.data, safe=False)

class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
