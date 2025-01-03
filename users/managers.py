from django.db import models
from .models import UserProfile

class UserProfileManager(models.Manager):

  def for_user(user):
    return UserProfile.objects.get(user=user)
