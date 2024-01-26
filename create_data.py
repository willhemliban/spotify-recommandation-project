import pandas as pd
from utils.utils import playlist_to_dataframe

################ creating dataset

# giving playlist link
liked_playlist = playlist_to_dataframe("https://open.spotify.com/playlist/6m12tlCvhBeF6s9qzI6670?si=fb7b069056b04651")
disliked_playlist = playlist_to_dataframe("https://open.spotify.com/playlist/2VoQ77iUAuUTdcnBZtaOtk?si=d0093e15c4ea46ed")

# merging both playlists
df = pd.concat([liked_playlist, disliked_playlist], axis=0)

# creating a new column if the song is liked or not (1 = liked, 0 = disliked)
df["liked"] = [1] * len(liked_playlist) + [0] * len(disliked_playlist)

# saving dataframe as csv
df.to_csv("data/train_data.csv", index=False)

################ playlist to use the model on

# giving playlist link
df = playlist_to_dataframe("https://open.spotify.com/playlist/37i9dQZF1DZ06evO0A1rXi?si=7ec186d37c4e4010")

# saving dataframe as csv
df.to_csv("data/test_data.csv", index=False)