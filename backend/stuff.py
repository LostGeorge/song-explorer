import spotipy
from backend.api import get_sp_client

def get_rec_song_list(username, playlist_name, anchor_fp, ratio):
    sp = get_sp_client(['playlist-read-private'])
    playlists = sp.user_playlist(username)
    


