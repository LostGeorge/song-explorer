import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
sys.path.append('..')
from backend.auth import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

def get_sp_client(scopes):
    '''
    For the scope, check out
    https://developer.spotify.com/documentation/general/guides/authorization/scopes/
    '''
    auth_manager = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scopes
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)

    return sp

# Unit Testing
if __name__ == '__main__':

    sp = get_sp_client(['playlist-read-private'])
    playlists = sp.user_playlist('lost_herro')
    print(playlists)
    for playlist in playlists['items']:
        print(playlist['name'])
