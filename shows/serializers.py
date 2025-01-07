from rest_framework import serializers
from .models import Show
from images.serializers import ImageSerializer

class ShowsSerializer(serializers.ModelSerializer):
  thumbnail = ImageSerializer(many=False)
  class Meta:
    model = Show
    fields = ['id', 'venue', 'presale_link', 'has_presale', 'show_date_time', 'thumbnail']
    
class ShowSerializer(serializers.ModelSerializer):
  images = ImageSerializer(many=True)
  thumbnail = ImageSerializer(many=False)
  class Meta:
    model = Show
    fields = ['id', 'venue', 'presale_link', 'has_presale', 'show_date_time', 'thumbnail', 'images']
