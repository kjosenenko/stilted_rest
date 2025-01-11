from django.db import models
from bands.models import Band

class Music(models.Model):
    name = models.CharField(max_length=128)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    album_id = models.CharField(max_length=32, blank=True, null=True)  # For albums
    track_id = models.CharField(max_length=32, blank=True, null=True)  # For singles
    bandcamp_url = models.URLField()  # Direct link to the song/album
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "music"
