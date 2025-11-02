
import os
import pandas as pd
import numpy as np

CSV_PATH = os.getenv("SPOTIFY_CSV", "./data/SpotifyFeatures.csv")
_df = pd.read_csv(CSV_PATH)

for col in ["valence", "energy", "danceability", "tempo", "popularity"]:
    if col in _df.columns:
        _df[col] = pd.to_numeric(_df[col], errors="coerce")

EMOTION_TO_PROFILE = {
    "joy": {"valence": (0.7, 1.0), "energy": (0.5, 1.0)},
    "surprise": {"valence": (0.6, 1.0), "energy": (0.6, 1.0)},
    "anger": {"valence": (0.0, 0.4), "energy": (0.7, 1.0)},
    "fear": {"valence": (0.0, 0.3), "energy": (0.3, 0.7)},
    "sadness": {"valence": (0.0, 0.3), "energy": (0.0, 0.5)},
    "neutral": {"valence": (0.4, 0.6), "energy": (0.3, 0.6)},
}

def _filter_by_profile(df, emotion):
    prof = EMOTION_TO_PROFILE.get(emotion, EMOTION_TO_PROFILE["neutral"])
    mask = np.logical_and.reduce([
        (df[k] >= v[0]) & (df[k] <= v[1]) for k, v in prof.items() if k in df.columns
    ])
    sub = df[mask]
    return sub if len(sub) else df.sample(min(50, len(df)))

def recommend(emotion, k=10):
    sub = _filter_by_profile(_df, emotion)
    prof = EMOTION_TO_PROFILE.get(emotion, EMOTION_TO_PROFILE["neutral"])
    def score_row(r):
        return sum(abs(r[feat] - np.mean(bounds)) for feat, bounds in prof.items() if feat in r)
    sub["rank_score"] = sub.apply(score_row, axis=1)
    return sub.sort_values("rank_score").head(k)[
        ["track_name","artist_name","valence","energy","danceability","tempo","popularity"]
    ]
