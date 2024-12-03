from rest_framework import serializers
from .models import Contact

class SubmissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ['id', 'name', 'email', 'phone', 'band']