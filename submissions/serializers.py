from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Submission
    fields = ['id', 'contact_name', 'contact_email', 'contact_phone', 'message_subject', 'message_body']
