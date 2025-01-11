from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from bands.models import Band

def show_flyer_path(instance, filename):
    """Generate path for show flyer"""
    return f'shows/{instance.venue.id}/{filename}'

class Venue(models.Model):
    name = models.CharField(max_length=128)
    street_address = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, help_text="Any additional information about the venue")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'city', 'state']

    @property
    def full_address(self):
        """Returns the complete formatted address"""
        parts = [self.street_address]
        if self.city and self.state:
            parts.append(f"{self.city}, {self.state}")
        if self.zip_code:
            parts.append(self.zip_code)
        return " ".join(filter(None, parts))

    @property
    def location(self):
        """Returns just the city and state"""
        if self.city and self.state:
            return f"{self.city}, {self.state}"
        return ""

class Show(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT, related_name='shows')
    doors_at = models.DateTimeField(null=True, blank=True, help_text="When doors open")
    starts_at = models.DateTimeField(null=True, blank=True, help_text="When the show starts")
    ticket_price = models.CharField(max_length=64, blank=True)
    presale_link = models.URLField(blank=True, null=True)
    has_presale = models.BooleanField(default=False)
    age_restriction = models.CharField(max_length=32, blank=True)
    supporting_acts = models.TextField(blank=True)
    description = models.TextField(blank=True)
    flyer = models.ImageField(upload_to=show_flyer_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.starts_at.strftime('%Y-%m-%d %H:%M') if self.starts_at else 'TBD'} at {self.venue.name}"

    class Meta:
        ordering = ['starts_at']

    def clean(self):
        if self.doors_at and self.starts_at and self.doors_at > self.starts_at:
            raise ValidationError('Doors time must be before show start time')
