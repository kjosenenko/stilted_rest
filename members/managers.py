from django.db import models
from .models import Member

class MemberManager(models.Manager):

  def band_members(band):
    return Member.objects.filter(band=band)
