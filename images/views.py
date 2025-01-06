from django.http import JsonResponse
# from .managers import ImageManager
from .serializers import ImageSerializer
from bands.managers import BandManager

def images(request):
  if request.method == 'GET':
    return JsonResponse({"error": "Band not found."}, status=404)
    # to do - work out the polymorphic manager
    band = BandManager.find_by_request(request)
    if not band:
      return JsonResponse({"error": "Band not found."}, status=404)
    else:
      serializer = ImageSerializer(ImageManager.images_for_band(band), many=True)
      return JsonResponse(serializer.data, safe=False)
