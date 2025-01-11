from rest_framework import serializers
from .models import Band

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name', 'url', 'bio', 'email', 
                 'logo', 'logo_alt', 'cover_photo', 'cover_photo_alt']
