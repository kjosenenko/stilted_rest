from django.db import models
import os

def band_logo_path(instance, filename):
    """Generate path for band logos"""
    ext = filename.split('.')[-1]
    # Force lowercase for filesystem path
    band_name = instance.name.lower()
    return f'bands/{band_name}/logo.{ext}'

def band_cover_path(instance, filename):
    """Generate path for band cover photos"""
    ext = filename.split('.')[-1]
    # Force lowercase for filesystem path
    band_name = instance.name.lower()
    return f'bands/{band_name}/cover.{ext}'

def band_gallery_path(instance, filename):
    """Generate path for band gallery images"""
    # Force lowercase for filesystem path
    band_name = instance.name.lower()
    return f'bands/{band_name}/gallery/{filename}'

class Band(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    email_password = models.CharField(max_length=128, blank=True, null=True)
    smtp_server = models.CharField(max_length=128, blank=True, null=True)
    smtp_port = models.IntegerField(blank=True, null=True)
    
    # Image fields
    logo = models.ImageField(upload_to=band_logo_path, blank=True, null=True)
    logo_alt = models.CharField(max_length=128, blank=True, help_text="Alt text for the band's logo")
    cover_photo = models.ImageField(upload_to=band_cover_path, blank=True, null=True)
    cover_photo_alt = models.CharField(max_length=128, blank=True, help_text="Alt text for the band's cover photo")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete image files when band is deleted
        if self.logo:
            if os.path.isfile(self.logo.path):
                os.remove(self.logo.path)
        if self.cover_photo:
            if os.path.isfile(self.cover_photo.path):
                os.remove(self.cover_photo.path)
        super().delete(*args, **kwargs)

    @property
    def cover_photo_url(self):
        if self.cover_photo:
            return f'/api{self.cover_photo.url}'
        return None
