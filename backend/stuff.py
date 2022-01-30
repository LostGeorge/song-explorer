import spotipy
import numpy as np
import json, sys
sys.path.append('..')
from backend.api import get_sp_client
from backend.anchors import ratio_to_distance, find_shell_point_ids, FEATURE_IDX_MAP

def get_input_features(track_lst, sp):
    feat_dicts = sp.audio_features(tracks=track_lst)
    input_feats = np.zeros((len(track_lst), len(FEATURE_IDX_MAP)))
    for i in range(len(track_lst)):
        for feat, idx in FEATURE_IDX_MAP.items():
            input_feats[i, idx] = feat_dicts[i][feat]
    return input_feats

def get_rec_song_list(username, playlist_name, anchor_fp, ratio):
    track_id_lst = []
    sp = get_sp_client(['playlist-read-private'])
    playlists = sp.user_playlists(username)
    playlist_dict = [playlst for playlst in playlists['items'] if playlst['name'] == playlist_name][0]
    results = sp.playlist(playlist_dict['id'], fields='tracks,next')
    tracks = results['tracks']
    for item in tracks['items']:
        track_id_lst.append(item['track']['id'])
    while tracks['next']:
        tracks = sp.next(tracks)
        for item in tracks['items']:
            track_id_lst.append(item['track']['id'])
            

    input_features = get_input_features(track_id_lst, sp)
    anchor_features = np.load(f'{anchor_fp}.npy')
    anchor_ids = json.load(f'{anchor_fp}.json')
    rec_ids = find_shell_point_ids(input_features, anchor_features,
        anchor_ids, shell_dist=ratio_to_distance(ratio))
    
    ret_lst = []
    for rec_id in rec_ids:
        track = sp.track(rec_id)
        ret_lst.append({
            'Artist': track['artists'][0]['name'],
            'Song Title': track['name'],
            'Link': track['external_urls']['spotify']
        })
    return ret_lst


if __name__ == '__main__':
    rec_songs = get_rec_song_list('lost_herro', 'Potpurri', 'test', 0.2)
    print(rec_songs)


