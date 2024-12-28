from django.db import models
from django.contrib.auth.models import AbstractUser
from bands.models import Band

class CustomUser(AbstractUser):
    bands = models.ManyToManyField(Band, null=True, blank=True, default=None)
    pass

    def __str__(self):
        return self.email
 