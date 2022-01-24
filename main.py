import urllib.request
import json


def format_output(list):
    for item in list:
        print(item)


with urllib.request.urlopen("https://api.ampifymusic.com/packs") as url_json:
    data = json.loads(url_json.read().decode())

songs = data['packs']
genres = []
all_genres = []

for song in songs:
    for genre in song['genres']:
        if genre in genres:
            continue
        genres.append(genre)

format_output(genres)