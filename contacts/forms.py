from django import forms
from bands.models import Band

class ContactForm(forms.Form):
  name = forms.CharField(max_length=128, required=True)
  email = forms.EmailField(required=True)
  phone = forms.CharField(max_length=128, required=False)
  message_subject = forms.CharField(max_length=128, required=True)
  message_body = forms.CharField(required=True)
  band_id = forms.IntegerField(required=True)
  add_to_mailer = forms.BooleanField(required=False)
