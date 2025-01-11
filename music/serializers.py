from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    embed_url = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = ['id', 'name', 'embed_url', 'bandcamp_url']

    def get_embed_url(self, obj):
        base_url = "https://bandcamp.com/EmbeddedPlayer"
        params = {
            'size': 'large',
            'bgcol': '333333',
            'linkcol': 'e32c14',
            'transparent': 'true',
            'artwork': 'small'
        }
        
        if obj.album_id:
            params['album'] = obj.album_id
            params['tracklist'] = 'true'  # Show the tracklist
        else:
            params['track'] = obj.track_id
            params['tracklist'] = 'false'

        param_string = '/'.join(f"{k}={v}" for k, v in params.items())
        return f"{base_url}/{param_string}/"