from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from bands.models import Band

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(
        "users.CustomUser",
        on_delete=models.CASCADE,
    )
    bands = models.ManyToManyField(Band, null=True, blank=True, default=None)

    def __str__(self):
        return f"Profile for {self.user.email}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if instance.is_superuser:
        return
    else:
        UserProfile.objects.get_or_create(user=instance)
