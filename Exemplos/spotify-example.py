# pip install spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# the file save.py must be in the same folder
from save import Saver
import csv


# Go to the Dashboard at developer.spotify.com and
# create an app. You will receive an id and secret.
CLIENT_ID = r'5fbcebb484074f9d90a2fd7c1392a6d1'
CLIENT_SECRET = r'6b3094e8770a46c6b82fee98a24386c8'

# # Go to the Spotify webplayer and go the artist
# # page. The id should be at the address bar.
# EGO_USERNAME = r'4dpARuHxo51G3z768sgnrY'

OUTPUT_PATH = r'spotify'


def get_name(api, ego_username):
    artist = api.artist(ego_username)
    return artist['name']


def get_usernames(api, ego_username):
    related = api.artist_related_artists(ego_username)
    artists = related['artists']
    return [artist['id'] for artist in artists]


def main():
    lista_ids = []
    lista_nomes = []
    with open('caches_spotify.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')

        for row in readCSV:
            id_artista = row[3]
            nome = row[0]
            lista_ids.append(id_artista)
            lista_nomes.append(nome)


    
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    api = Spotify(client_credentials_manager=client_credentials_manager)

    tam = 0
    while tam in range(len(lista_ids)):
        
        EGO_USERNAME = lista_ids[tam]
        
        OUTPUT_PATH = lista_nomes[tam]

        saver = Saver(OUTPUT_PATH)

        name = get_name(api, EGO_USERNAME)

        usernames = get_usernames(api, EGO_USERNAME)

        print(usernames)

        saver.save(EGO_USERNAME, name, usernames)

        for username in usernames:
            name = get_name(api, username)

            alter_usernames = get_usernames(api, username)
            #print(alter_usernames)

           # saver.save(username, name, alter_usernames)
        
        tam += 1


if __name__ == '__main__':
    main()
