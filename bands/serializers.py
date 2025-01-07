from rest_framework import serializers
from .models import Band
from images.serializers import ImageSerializer

class BandSerializer(serializers.ModelSerializer):
  cover_photo = ImageSerializer(many=False)
  logo = ImageSerializer(many=False)
  class Meta:
    model = Band
    fields = ['id', 'name', 'url', 'bio', 'cover_photo', 'logo']
    
class BandImagesSerializer(serializers.ModelSerializer):
  images = ImageSerializer(many=True)
  cover_photo = ImageSerializer(many=False)
  logo = ImageSerializer(many=False)
  class Meta:
    model = Band
    fields = ['id', 'name', 'url', 'bio', 'cover_photo', 'logo', 'images']
