from django.db import models
from .models import Member
from users.models import CustomUser

class MemberManager(models.Manager):

  def band_members(band):
    return Member.objects.filter(band=band)
  
  # TO DO: add a for user scope.
  def for_user(user):
    breakpoint()
