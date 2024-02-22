from django.core.management.base import BaseCommand
from shows.models import Show

class Command(BaseCommand):
    help = 'Remove images for past shows'

    def handle(self, *args, **kwargs):
      Show.cleanup()
