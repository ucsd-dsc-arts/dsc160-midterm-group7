import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import urllib.request



cid = '5c3d73b1e0734983aec11219f14fef4f'
secret = 'f23dddb03f9a4097887e4a251758f86d'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)



def get_artist(name):
    """
    Get artist information based on name
    """
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None
    
def show_recommendations_for_artist(artist):
    results = sp.recommendations(seed_artists=[artist['id']])
    tracks = {}
    for track in results['tracks']:
        tracks[track['name']] = track['artists'][0]['name']
        print('Recommendation: %s - %s', track['name'],
                    track['artists'][0]['name'])
    return tracks

def show_artist_albums(artist):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    return results['items']

def get_tracks_from_album(album):
    uri  = album['uri']
    return sp.album_tracks(uri)['items']

def show_artist(artist):
    print('Name ', artist['name'])
    print('Popularity: %s' % artist['popularity'])
    if len(artist['genres']) > 0:
        print('Genres: %s' % artist['genres'])
        
        
def top_songs(artist):
    results = sp.artist_top_tracks(artist['id'])
    return results['tracks']

def download_track(track, directory):
    if track['preview_url'] != None:
        url = track['preview_url']
        if not os.path.isdir(directory):
            os.mkdir(directory)
        
        name = directory + '/' + track['name'] + '.mp4'
        urllib.request.urlretrieve(url, name)
    else:
        name =  track['name']
        print('No Preview URL found for track - %s'%name) 
    
