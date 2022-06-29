import os
import requests
from pyyoutube import Api

API_KEY = os.environ.get('YOUTUBE_API_KEY')
api = Api(api_key=API_KEY)

channel_id = "UC39a9uWnGIDYzi5BMndFmiw"
channel_info = api.get_channel_info(channel_id=channel_id)

playlist_id = channel_info.items[0].contentDetails.relatedPlaylists.uploads

uploads_playlist_items = api.get_playlist_items(
    playlist_id=playlist_id, count=10, limit=6
)

videos = []
for item in uploads_playlist_items.items:
    videos.append(item.snippet.title)

print(videos)
