from colorama import Fore as Colour
from spotipy.oauth2 import SpotifyOAuth
import spotipy.client as spotipy

CLIENT_ID, CLIENT_SECRET = "", ""
REDIRECT_URI = "http://localhost:8888"
MAX = 10

scope = "playlist-modify-public"

client = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    scope=scope,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI
))

print(f"{Colour.LIGHTGREEN_EX}compiling your playlists...{Colour.RESET}")
playlists = []
# get all playlists
for x in range(0, MAX):
    new = client.current_user_playlists(50, offset=x*50)["items"]
    if len(new) > 0:
        playlists += new
    else:
        break

print(f"{Colour.LIGHTGREEN_EX}creating a list of all of your songs...{Colour.RESET}")
# get all tracks
tracks = []
for playlist in playlists:
    for x in range(0, MAX):
        new = client.playlist_tracks(playlist["id"], limit=100, offset=x*100)["items"]
        if len(new) > 0:
            for t in new:
                if t not in tracks:
                    tracks.append(t["track"])
        else:
            break

# create new playlist
playlist = client.user_playlist_create(client.current_user()["id"], name="spotistash", description="https://github.com/jibstack64/spotistash")

print(f"{Colour.LIGHTGREEN_EX}adding tracks to new playlist...{Colour.RESET}")
# add tracks
layers = [[]]
x = 0
l = 0
for track in tracks:
    if x % 100:
        l += 1
        layers.append([])
    layers[l].append(track)
    x += 1
for layer in layers:
    client.playlist_add_items(playlist["id"], [track["id"] for track in layer])

print(f"{Colour.LIGHTGREEN_EX}done, here's your playlist: {Colour.LIGHTMAGENTA_EX}{playlist['external_urls']['href']}{Colour.RESET}")
