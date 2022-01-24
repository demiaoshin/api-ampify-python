import urllib.request
import json


def format_output(list):
    for item in list:
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
all_genres = []
hip_hop_packs = []
count = 0
set_of_genres = {}
temp = []

for song in songs:
    for genre in song['genres']:
        if genre in genres:
            continue
        if genre == "hip-hop":
            hip_hop_packs.append(song)
            count += 1
        genres.append(genre)

for song in songs:
    for genre in genres:
        if genre in song['genres']:
            temp.append(song)
        set_of_genres[genre] = temp

print("LIST OF ALL GENRES:")
format_output(genres)

print("LIST OF ALL PACKS WITH THE GENRE 'HIP-HOP':")
# There is only one song that has the genre hip hop so we print out the only song here
format_song(hip_hop_packs[0])

