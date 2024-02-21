from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Submission(models.Model):
  contact_name = models.CharField(max_length=128, blank=True, null=True)
  contact_email = models.CharField(max_length=128, blank=True, null=True)
  contact_phone = models.CharField(max_length=128, blank=True, null=True)
  message_subject = models.CharField(max_length=128, blank=True, null=True)
  message_body = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
@receiver(post_save, sender=Submission)
def send_email(sender, instance, **kwargs):
  print(instance.contact_name)
  print(instance.contact_email)
  print(instance.contact_phone)
  print(instance.message_subject)
  print(instance.message_body)
