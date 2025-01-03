from django.db import models
from .models import Member
from users.managers import UserProfileManager

class MemberManager(models.Manager):

  def band_members(band):
    return Member.objects.filter(band=band)

  def for_user(user):
    profile = UserProfileManager.for_user(user)
    return Member.objects.filter(band__in=[x.id for x in profile.bands.all()])
