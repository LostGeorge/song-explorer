import spotipy
import numpy as np
import random
import sys, json
from backend.api import get_sp_client

FEATURE_IDX_MAP = dict(zip(['acousticness', 'danceability', 'energy', 'instrumentalness',
                            'liveness', 'mode', 'speechiness', 'valence', 'tempo'], range(9)))

def generate_anchors(output_fp_base, n_per_genre=100):

    sp = get_sp_client(scopes=[])
    genres = sp.recommendation_genre_seeds()['genres']
    anchor_features = np.zeros((len(genres) * n_per_genre, len(FEATURE_IDX_MAP)))
    anchor_ids = []
    for i, genre in enumerate(genres):
        genre_anchors = sp.recommendations(seed_genres=[genre], limit=n_per_genre)
        genre_song_ids = [anchor_dict['id'] for anchor_dict in genre_anchors['tracks']]
        anchor_ids.extend(genre_song_ids)
        genre_feat_dicts = sp.audio_features(tracks=genre_song_ids)
        for j in range(n_per_genre):
            for feat, idx in FEATURE_IDX_MAP.items():
                anchor_features[i*n_per_genre+j, idx] = genre_feat_dicts[j][feat]
    anchor_features[:, -1] /= 250
    np.save(f'{output_fp_base}.npy', anchor_features)
    json.dump(anchor_ids, f'{output_fp_base}.json')

def find_shell_point_ids(input_features, anchor_features, anchor_ids, shell_dist=1, n_samp=10):
    n = len(input_features)
    input_sampled = input_features[random.sample(range(n), max(n_samp, n)), :]
    input_3d = np.tile(input_sampled[:, None, :], (1, len(anchor_features), 1))
    distance_mat = np.sqrt(np.sum((input_3d - anchor_features)**2, axis=2))
    shell_distances = np.abs(distance_mat - shell_dist)
    best_shell_idxs = set(np.argmin(shell_distances, axis=1))
    return [anchor_id for i, anchor_id in enumerate(anchor_ids) if i in best_shell_idxs]

def ratio_to_distance(r):
    return r * 1.5

if __name__ == '__main__':
    generate_anchors('test.npy', 2)
    

