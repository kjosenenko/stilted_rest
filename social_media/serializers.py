from rest_framework import serializers
from .models import SocialMedia

class SocialMediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = SocialMedia
    fields: list[str] = ['id', 'provider', 'href']