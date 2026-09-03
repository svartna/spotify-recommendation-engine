import requests
from auth import get_access_token


access_token = get_access_token()

headers = {"Authorization": f"Bearer {access_token}"}
top_tracks = requests.get("https://api.spotify.com/v1/me/top/tracks", headers=headers)

# print a readable song list

data = top_tracks.json()

for track in data["items"]:
    track_name = track["name"]
    artist_name = track["artists"][0]["name"]
    print(f"{track_name} ~ {artist_name}")
