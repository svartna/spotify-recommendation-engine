import pandas as pd
from get_top_tracks import get_top_tracks
from curated_genres import ARTIST_GENRES

def build_feature_rows():
    data = get_top_tracks()
    tracks_with_features = []

    for track in data["items"]:
        artist_id = track["artists"][0]["id"]
        tracks_with_features.append({
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "genres": ARTIST_GENRES.get(artist_id, ["unkown"]),
            "duration_ms": track["duration_ms"],
            "explicit": track["explicit"],
            "release_date": track["album"]["release_date"],
        })

    return tracks_with_features

def ms_to_minutes_seconds(ms):
    total_seconds = ms // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"

def explicit_label(is_explicit):
    return "Yes" if is_explicit else "No"

def build_feature_dataframe():
    rows = build_feature_rows()
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = build_feature_dataframe()
    df["duration"] = df["duration_ms"].apply(ms_to_minutes_seconds)
    df["explicit?"] = df["explicit"].apply(explicit_label)
    df["release date"] = df["release_date"]
    print(df[["name", "artist", "duration", "explicit?", "release date"]])
