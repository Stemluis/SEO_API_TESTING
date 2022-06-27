import os
import requests

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'
track_url = input('Enter track url: ')
track_id = track_url.replace('https://open.spotify.com/track/', '')
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
print(r.json())

ids = []
for i in range(5):
    ids.append(input(f"Enter track #{i} url: ").replace('https://open.spotify.com/track/', ''))

PARAMS = {'seed_track':ids}
recommend = requests.get(BASE_URL + 'recommendations/', headers=headers, params = PARAMS)
print(recommend.json())


# recommendations = requests.get(BASE_URL + '/recommendations/', headers=headers)