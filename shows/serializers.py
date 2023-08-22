from rest_framework import serializers
from .models import Show

class ShowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Show
    fields = ['id', 'venue', 'presale_link', 'has_presale', 'supporting_acts', 'show_date_time', 'image']
