from playlist import Playlist
from Song import Song


def create_playlist(filename_1, playlist_1, type_1):
    file = open(filename_1, "r")
    l = []
    li = file.readlines()
    for i in range(len(li)):
        l.append(li[i].split("\t"))
    for song in l:
        if song[3][:len(song[3])-1] == type_1:
            playlist_1.add_song(Song(song[0], song[1], song[2]))


name = "April2020GymHits"
purpose = "workout"
filename = 'April2020GymHits.txt'
song_list = []
length = 0
playlist = Playlist(name, purpose, length, song_list)
create_playlist(filename, playlist, purpose)
playlist.bubbleSort()
print(playlist)
duration = int(input("Enter duration of song: "))
index = playlist.binary_search(0, playlist.get_num_songs()-1, duration)
if index != -1:
    print("Song with duration " + str(duration) + " " + str(playlist.get_song(index)))
else:
    print("No song exists with duration equals to " + str(duration) + "\n")
playlist.sort_playlist()
print("Default sorted playlist:", playlist)
