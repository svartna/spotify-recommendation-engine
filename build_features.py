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

if __name__ == "__main__":
    rows = build_feature_rows()
    print(rows[0])
