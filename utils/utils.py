import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

SPOTIPY_CLIENT_ID = "aee70dd0fbc64f339eb03597a1788ad7"
SPOTIPY_CLIENT_SECRET = "7606f1bd1bb44bd4bfd015c2679cee68"

# connecting with spotify api
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def playlist_to_dataframe(playlist_code):

    playlist_dict = sp.playlist(playlist_code)
    
    # getting all tracks from playlist
    tracks = playlist_dict["tracks"]["items"]

    # getting all tracks names
    tracks_names = []
    for track in tracks:
        tracks_names.append(track["track"]["name"])

    # getting all tracks artists
    tracks_artists = []
    for track in tracks:
        tracks_artists.append(track["track"]["artists"][0]["name"])

    # getting all tracks ids
    tracks_ids = []
    for track in tracks:
        tracks_ids.append(track["track"]["id"])

    # getting all tracks features
    tracks_features = []
    for track_id in tracks_ids:
        tracks_features.append(sp.audio_features(track_id)[0])

    # getting all tracks features names
    tracks_features_names = []
    for track_feature in tracks_features[0]:
        tracks_features_names.append(track_feature)

    # getting all tracks features values
    tracks_features_values = []
    for track_feature in tracks_features:
        tracks_features_values.append(list(track_feature.values()))

    # creating a dataframe with all tracks features
    df = pd.DataFrame(tracks_features_values, columns=tracks_features_names)

    # creating a dataframe with all tracks names and artists
    df_tracks = pd.DataFrame({"name": tracks_names, "artist": tracks_artists})

    # merging both dataframes while excluding the track id, uri, and url
    df = df.drop(["id", "uri", "track_href", "analysis_url","type"], axis=1)
    df = pd.concat([df_tracks, df], axis=1)

    return df