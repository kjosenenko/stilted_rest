from django.db import models

class ContactMessages(models.Model):
  contact_name = models.CharField(max_length=128, blank=True, null=True)
  contact_email = models.CharField(max_length=128, blank=True, null=True)
  contact_phone = models.CharField(max_length=128, blank=True, null=True)
  message_subject = models.CharField(max_length=128, blank=True, null=True)
  message_body = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
