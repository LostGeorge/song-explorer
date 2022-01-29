import spotipy
from spotipy.oauth2 import SpotifyOAuth

from auth import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

def get_auth_manager(scope):
    '''
    For the scope, check out
    https://developer.spotify.com/documentation/general/guides/authorization/scopes/
    '''
    auth_manager = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope
    )

    return auth_manager

# Unit Testing
if __name__ == '__main__':

    sp = spotipy.Spotify(auth_manager=get_auth_manager('playlist-read-private'))
    playlists = sp.user_playlist('lost_herro')
    for playlist in playlists['items']:
        print(playlist['name'])
