import urllib.request
import json


def format_output(arr):
    for item in arr:
        print(item)


def format_song(song):
    print(f"ID: {song['id']}\n"
          f"Itunes ID: {song['itunesId']}\n"
          f"Date Added: {song['dateAdded']}\n"
          f"Name: {song['name']}\n"
          f"Plans: {song['plans']}\n"
          f"Genres: {song['genres']}\n"
          f"Published?: {song['published']}\n")


with urllib.request.urlopen("https://api.ampifymusic.com/packs") as url_json:
    data = json.loads(url_json.read().decode())

songs = data['packs']

genres = []
hip_hop_packs = []

for song in songs:
    for genre in song['genres']:
        genres.append(genre)
        if genre == "hip-hop":
            hip_hop_packs.append(song)

genres = sorted(set(genres))

print("LIST OF ALL GENRES:")
format_output(genres)

print("LIST OF ALL PACKS WITH THE GENRE 'HIP-HOP':")
for song in hip_hop_packs:
    format_song(song)

