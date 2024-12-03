from django.core.management.base import BaseCommand
from shows.managers import ShowManager

class Command(BaseCommand):
    help = 'Remove images for past shows'

    def handle(self, *args, **kwargs):
      ShowManager.cleanup()
