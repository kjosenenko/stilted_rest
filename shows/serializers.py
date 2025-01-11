from rest_framework import serializers
from .models import Show, Venue

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['id', 'name', 'street_address', 'city', 'state', 
                 'zip_code', 'website', 'notes']

class ShowsSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)
    location = serializers.CharField(read_only=True)
    full_address = serializers.CharField(read_only=True)
    
    class Meta:
        model = Show
        fields = ['id', 'venue', 'doors_at', 'starts_at', 'ticket_price',
                'presale_link', 'has_presale', 'age_restriction',
                'supporting_acts', 'description', 'flyer', 'location', 'full_address']

class ShowSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)
    location = serializers.CharField(read_only=True)
    full_address = serializers.CharField(read_only=True)

    class Meta:
        model = Show
        fields = ['id', 'venue', 'doors_at', 'starts_at', 'ticket_price',
                'presale_link', 'has_presale', 'age_restriction',
                'supporting_acts', 'description', 'flyer', 'location', 'full_address']
