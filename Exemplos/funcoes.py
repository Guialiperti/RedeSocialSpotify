# pip install spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = r'5fbcebb484074f9d90a2fd7c1392a6d1'
CLIENT_SECRET = r'6b3094e8770a46c6b82fee98a24386c8'
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

api = Spotify(client_credentials_manager=client_credentials_manager)

def get_name(api, ego_username):
    artist = api.artist(ego_username)
    #print(artist['name'])
    return artist['name']


def get_usernames(api, ego_username):
    related = api.artist_related_artists(ego_username)
    artists = related['artists']
    return [artist['id'] for artist in artists]

def get_genres_artist(api, ego_username):
    artist = api.artist(ego_username)
    genres = artist['genres']
    return genres

def get_popularity_artist(api, ego_username):
    artist = api.artist(ego_username)
    popularity = artist['popularity']
    return popularity
