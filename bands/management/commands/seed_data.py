"""
Management command to generate seed data for all models in development.
Usage: python manage.py seed_data
"""
from django.core.management.base import BaseCommand, CommandParser
from django.utils import timezone
from datetime import timedelta
import random
from typing import Any

from bands.models import Band
from members.models import Member
from music.models import Music
from contacts.models import Contact
from social_media.models import SocialMedia
from shows.models import Venue, Show


class Command(BaseCommand):
    help = 'Generate seed data for development'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )

    def handle(self, *args: Any, **options: Any) -> None:
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Show.objects.all().delete()
            Venue.objects.all().delete()
            SocialMedia.objects.all().delete()
            Contact.objects.all().delete()
            Music.objects.all().delete()
            Member.objects.all().delete()
            Band.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('✓ Data cleared'))

        self.stdout.write('Generating seed data...')
        
        # Create Bands
        bands_data = [
            {
                'name': 'Stilted',
                'url': 'https://stilted.band',
                'bio': 'An experimental post-punk band pushing the boundaries of sound and rhythm.',
                'email': 'contact@stilted.band',
                'logo_alt': 'Stilted band logo',
                'cover_photo_alt': 'Stilted performing live',
            },
            {
                'name': 'The Echoes',
                'url': 'https://theechoes.band',
                'bio': 'Indie rock band with dreamy soundscapes and introspective lyrics.',
                'email': 'info@theechoes.band',
                'logo_alt': 'The Echoes logo',
                'cover_photo_alt': 'The Echoes band photo',
            },
            {
                'name': 'Neon Pulse',
                'url': 'https://neonpulse.band',
                'bio': 'Electronic synth-wave duo creating nostalgic yet futuristic sounds.',
                'email': 'hello@neonpulse.band',
                'logo_alt': 'Neon Pulse logo',
                'cover_photo_alt': 'Neon Pulse cover art',
            },
            {
                'name': 'Velvet Storm',
                'url': 'https://velvetstorm.band',
                'bio': 'High-energy rock band with a touch of psychedelic flair.',
                'email': 'contact@velvetstorm.band',
                'logo_alt': 'Velvet Storm logo',
                'cover_photo_alt': 'Velvet Storm live performance',
            },
        ]
        
        bands = []
        for band_data in bands_data:
            band, created = Band.objects.get_or_create(
                name=band_data['name'],
                defaults=band_data
            )
            bands.append(band)
            if created:
                self.stdout.write(f'  ✓ Created band: {band.name}')
            else:
                self.stdout.write(f'  → Band already exists: {band.name}')

        # Create Members
        members_data = [
            {'band': bands[0], 'name': 'Alex Rivera', 'instrument': 'Vocals, Guitar', 'bio': 'Founding member with 10 years of experience in the punk scene.'},
            {'band': bands[0], 'name': 'Sam Chen', 'instrument': 'Bass', 'bio': 'Jazz-trained bassist bringing groove to the chaos.'},
            {'band': bands[0], 'name': 'Jordan Blake', 'instrument': 'Drums', 'bio': 'Powerhouse drummer with a background in metal.'},
            {'band': bands[1], 'name': 'Maya Thompson', 'instrument': 'Lead Vocals', 'bio': 'Ethereal voice that haunts and heals.'},
            {'band': bands[1], 'name': 'Lucas Martinez', 'instrument': 'Guitar, Synth', 'bio': 'Multi-instrumentalist creating atmospheric textures.'},
            {'band': bands[1], 'name': 'Taylor Kim', 'instrument': 'Drums', 'bio': 'Precision drummer with a soft touch.'},
            {'band': bands[2], 'name': 'Casey Morgan', 'instrument': 'Synthesizers, Programming', 'bio': 'Electronic music producer obsessed with vintage synths.'},
            {'band': bands[2], 'name': 'River Stone', 'instrument': 'Vocals, Keyboard', 'bio': 'Vocalist with a passion for 80s aesthetics.'},
            {'band': bands[3], 'name': 'Dakota Ellis', 'instrument': 'Lead Guitar', 'bio': 'Shredder with psychedelic sensibilities.'},
            {'band': bands[3], 'name': 'Phoenix Wright', 'instrument': 'Lead Vocals', 'bio': 'Dynamic frontperson with powerful stage presence.'},
        ]
        
        for member_data in members_data:
            Member.objects.get_or_create(
                band=member_data['band'],
                name=member_data['name'],
                defaults=member_data
            )
        self.stdout.write(f'  ✓ Created {len(members_data)} members')

        # Create Music
        music_data = [
            {'band': bands[0], 'name': 'Fractured Reality', 'album_id': '12345', 'bandcamp_url': 'https://stilted.bandcamp.com/album/fractured-reality'},
            {'band': bands[0], 'name': 'Static Dreams', 'track_id': '67890', 'bandcamp_url': 'https://stilted.bandcamp.com/track/static-dreams'},
            {'band': bands[0], 'name': 'Echoes in the Void', 'album_id': '11111', 'bandcamp_url': 'https://stilted.bandcamp.com/album/echoes-in-the-void'},
            {'band': bands[1], 'name': 'Whispers & Shadows', 'album_id': '22222', 'bandcamp_url': 'https://theechoes.bandcamp.com/album/whispers-shadows'},
            {'band': bands[1], 'name': 'Midnight Sun', 'track_id': '33333', 'bandcamp_url': 'https://theechoes.bandcamp.com/track/midnight-sun'},
            {'band': bands[2], 'name': 'Synthwave Dreams', 'album_id': '44444', 'bandcamp_url': 'https://neonpulse.bandcamp.com/album/synthwave-dreams'},
            {'band': bands[2], 'name': 'Neon Nights', 'track_id': '55555', 'bandcamp_url': 'https://neonpulse.bandcamp.com/track/neon-nights'},
            {'band': bands[3], 'name': 'Thunder & Lightning', 'album_id': '66666', 'bandcamp_url': 'https://velvetstorm.bandcamp.com/album/thunder-lightning'},
        ]
        
        for music_item in music_data:
            Music.objects.get_or_create(
                band=music_item['band'],
                name=music_item['name'],
                defaults=music_item
            )
        self.stdout.write(f'  ✓ Created {len(music_data)} music items')

        # Create Contacts
        contacts_data = [
            {'band': bands[0], 'name': 'Sarah Johnson', 'email': 'sarah@stilted.band', 'phone': '555-0123'},
            {'band': bands[0], 'name': 'Mike Davis', 'email': 'mike@stilted.band', 'phone': '555-0124'},
            {'band': bands[1], 'name': 'Emily Wilson', 'email': 'emily@theechoes.band', 'phone': '555-0125'},
            {'band': bands[2], 'name': 'Chris Taylor', 'email': 'chris@neonpulse.band', 'phone': '555-0126'},
            {'band': bands[3], 'name': 'Jamie Anderson', 'email': 'jamie@velvetstorm.band', 'phone': '555-0127'},
        ]
        
        for contact_data in contacts_data:
            Contact.objects.get_or_create(
                band=contact_data['band'],
                email=contact_data['email'],
                defaults=contact_data
            )
        self.stdout.write(f'  ✓ Created {len(contacts_data)} contacts')

        # Create Social Media
        social_media_data = [
            {'band': bands[0], 'provider': 'Instagram', 'href': 'https://instagram.com/stiltedband'},
            {'band': bands[0], 'provider': 'Facebook', 'href': 'https://facebook.com/stiltedband'},
            {'band': bands[0], 'provider': 'Twitter', 'href': 'https://twitter.com/stiltedband'},
            {'band': bands[0], 'provider': 'Spotify', 'href': 'https://open.spotify.com/artist/stilted'},
            {'band': bands[1], 'provider': 'Instagram', 'href': 'https://instagram.com/theechoesband'},
            {'band': bands[1], 'provider': 'TikTok', 'href': 'https://tiktok.com/@theechoes'},
            {'band': bands[2], 'provider': 'Instagram', 'href': 'https://instagram.com/neonpulseband'},
            {'band': bands[2], 'provider': 'YouTube', 'href': 'https://youtube.com/neonpulse'},
            {'band': bands[3], 'provider': 'Instagram', 'href': 'https://instagram.com/velvetstormband'},
            {'band': bands[3], 'provider': 'Facebook', 'href': 'https://facebook.com/velvetstorm'},
        ]
        
        for social_data in social_media_data:
            SocialMedia.objects.get_or_create(
                band=social_data['band'],
                provider=social_data['provider'],
                defaults=social_data
            )
        self.stdout.write(f'  ✓ Created {len(social_media_data)} social media links')

        # Create Venues
        venues_data = [
            {
                'name': 'The Underground',
                'street_address': '123 Main St',
                'city': 'Portland',
                'state': 'OR',
                'zip_code': '97201',
                'website': 'https://theunderground.com',
                'notes': 'Intimate venue with great sound system',
            },
            {
                'name': 'Electric Avenue',
                'street_address': '456 Music Blvd',
                'city': 'Seattle',
                'state': 'WA',
                'zip_code': '98101',
                'website': 'https://electricavenue.com',
                'notes': 'Large capacity venue, 21+ only',
            },
            {
                'name': 'The Basement',
                'street_address': '789 Underground Way',
                'city': 'San Francisco',
                'state': 'CA',
                'zip_code': '94102',
                'website': 'https://thebasement.com',
                'notes': 'DIY space, all ages welcome',
            },
            {
                'name': 'Reverb Hall',
                'street_address': '321 Sound St',
                'city': 'Los Angeles',
                'state': 'CA',
                'zip_code': '90012',
                'website': 'https://reverbhall.com',
                'notes': 'Historic venue with excellent acoustics',
            },
            {
                'name': 'The Echo Chamber',
                'street_address': '654 Rock Lane',
                'city': 'Austin',
                'state': 'TX',
                'zip_code': '78701',
                'website': 'https://echochamber.com',
                'notes': 'Outdoor and indoor stages',
            },
        ]
        
        venues = []
        for venue_data in venues_data:
            venue, created = Venue.objects.get_or_create(
                name=venue_data['name'],
                city=venue_data['city'],
                state=venue_data['state'],
                defaults=venue_data
            )
            venues.append(venue)
        self.stdout.write(f'  ✓ Created {len(venues_data)} venues')

        # Create Shows (mix of past and future)
        shows_data = []
        now = timezone.now()
        
        # Past shows
        for i in range(5):
            days_ago = random.randint(30, 180)
            show_date = now - timedelta(days=days_ago)
            doors_time = show_date.replace(hour=19, minute=0, second=0, microsecond=0)
            start_time = doors_time + timedelta(hours=1)
            
            shows_data.append({
                'band': random.choice(bands),
                'venue': random.choice(venues),
                'doors_at': doors_time,
                'starts_at': start_time,
                'ticket_price': random.choice(['$10', '$15', '$20', 'Free']),
                'has_presale': random.choice([True, False]),
                'age_restriction': random.choice(['All Ages', '18+', '21+']),
                'supporting_acts': random.choice([
                    'Local band A, Local band B',
                    'The Openers',
                    'Supporting Act',
                    '',
                ]),
                'description': 'An unforgettable night of live music!',
            })
        
        # Future shows
        for i in range(8):
            days_ahead = random.randint(7, 90)
            show_date = now + timedelta(days=days_ahead)
            doors_time = show_date.replace(hour=19, minute=0, second=0, microsecond=0)
            start_time = doors_time + timedelta(hours=1)
            
            has_presale = random.choice([True, False])
            shows_data.append({
                'band': random.choice(bands),
                'venue': random.choice(venues),
                'doors_at': doors_time,
                'starts_at': start_time,
                'ticket_price': random.choice(['$12', '$15', '$18', '$20', '$25']),
                'presale_link': f'https://tickets.example.com/show-{i}' if has_presale else None,
                'has_presale': has_presale,
                'age_restriction': random.choice(['All Ages', '18+', '21+']),
                'supporting_acts': random.choice([
                    'Special guests TBA',
                    'The Newcomers, Rising Stars',
                    'Local favorites',
                    '',
                ]),
                'description': 'Join us for an amazing show! Tickets available now.',
            })
        
        for show_data in shows_data:
            Show.objects.get_or_create(
                band=show_data['band'],
                venue=show_data['venue'],
                starts_at=show_data['starts_at'],
                defaults=show_data
            )
        self.stdout.write(f'  ✓ Created {len(shows_data)} shows')

        self.stdout.write(self.style.SUCCESS('\n✓ Seed data generation complete!'))
        self.stdout.write(self.style.SUCCESS(f'\nSummary:'))
        self.stdout.write(f'  • {Band.objects.count()} bands')
        self.stdout.write(f'  • {Member.objects.count()} members')
        self.stdout.write(f'  • {Music.objects.count()} music items')
        self.stdout.write(f'  • {Contact.objects.count()} contacts')
        self.stdout.write(f'  • {SocialMedia.objects.count()} social media links')
        self.stdout.write(f'  • {Venue.objects.count()} venues')
        self.stdout.write(f'  • {Show.objects.count()} shows')
