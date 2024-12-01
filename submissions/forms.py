from django import forms
from bands.models import Band

class Submission(forms.Form):
  contact_name = forms.CharField(max_length=128, required=True)
  contact_email = forms.EmailField(required=True)
  contact_phone = forms.CharField(max_length=128, required=False)
  message_subject = forms.CharField(max_length=128, required=True)
  message_body = forms.CharField(required=True)
  band_id = forms.IntegerField(required=True)
  # add_to_mailer = forms.BooleanField(required=True)
  
  def send_email():
    breakpoint()
