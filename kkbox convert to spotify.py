import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# URL of the KKBOX song list you want to scrape
url = input('kkbox song list url:')

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the songlist name & description
playlist_name = soup.find('title').text
playlist_des = soup.find('meta', property="og:description", content = True)

# Find the song list container element
playlist_container = soup.find('div', class_='playlist-content')
info_container = playlist_container.find('div',class_= 'playlist-info')

# Find all the song list items
song_list_items = info_container.find_all('li')

# Set up Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                           client_id='your client_id',
                           client_secret='your client_secret',
                           redirect_uri='your redirect_uri',
                           scope = 'playlist-modify-private'))


# Converting KKBOX songlist to Spotify playlist
track_uris = []
for song_item in song_list_items:
    song_text = song_item.find('div', class_='text')
    album = song_text.find('div', class_='artist-album')
    artist_name = album.find('a').text
    song_title = song_text.find('div', class_='song').text
    result = sp.search(q=f"{song_title} {artist_name}", type='track', limit=1)
    if result['tracks']['items']:
        track_uris.append(result['tracks']['items'][0]['uri'])
        
# Creating Spotify playlist and adding tracks
playlist_description = playlist_des['content']
playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=playlist_name, public=False, description=playlist_description)
sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

