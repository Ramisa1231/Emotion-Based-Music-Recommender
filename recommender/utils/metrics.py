
import pandas as pd
import numpy as np

EXPECTED_VALENCE = {
    "joy": 0.85, "surprise": 0.65, "anger": 0.20,
    "fear": 0.25, "sadness": 0.30, "neutral": 0.50
}

def diversity_score(df):
    if df.empty: return 0.0
    return df["artist_name"].nunique() / len(df)

def novelty_score(df):
    if "popularity" not in df.columns or df.empty: return 0.5
    pop = df["popularity"].dropna()
    if pop.empty: return 0.5
    return float(1 - ((pop - pop.min()) / (pop.max() - pop.min())).mean())

def emotion_match_score(df, emotion):
    if df.empty or "valence" not in df.columns: return 0.0
    val = df["valence"].dropna()
    expected = EXPECTED_VALENCE.get(emotion, 0.5)
    return float(1 - abs(val.mean() - expected))

def correction_factor(user_profile, df):
    cf = 1.0
    if user_profile.get("prefers_uplifting"): cf += 0.05
    if user_profile.get("avoids_sad") and df["valence"].mean() < 0.35: cf -= 0.05
    if user_profile.get("novelty_seeking"): cf += 0.05
    return round(max(0.8, min(1.2, cf)), 3)
