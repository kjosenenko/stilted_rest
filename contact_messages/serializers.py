from rest_framework import serializers
from .models import ContactMessage

class ContactMessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactMessage
    fields = ['id', 'contact_name', 'contact_email', 'contact_phone', 'message_subject', 'message_body']
