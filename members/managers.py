from __future__ import annotations

from django.db import models
from .models import Member

class MemberManager(models.Manager):

  def band_members(band) -> models.QuerySet[Member]:
    return Member.objects.filter(band=band)
