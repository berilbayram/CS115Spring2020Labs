class Playlist:

    def __init__(self, name, purpose, length, song_list):
        self.__name = name
        self.__purpose = purpose
        self.__length = length
        self.__song_list = song_list

    def get_song(self, index):
        return self.__song_list[index]

    def get_num_songs(self):
        return len(self.__song_list)

    def add_song(self, song):
        if song not in self.__song_list:
            self.__song_list.append(song)
            self.__length = self.__length + song.get_duration()

    def bubbleSort(self):
        print("Bubble Sorted List: ", end="")
        sorted_list = []
        while len(self.__song_list) != 0:
            longest = self.__song_list[0]
            for i in range(len(self.__song_list)):
                if longest.get_duration() < self.__song_list[i].get_duration():
                    longest = self.__song_list[i]
            sorted_list.append(longest)
            self.__song_list.remove(longest)
        self.__song_list = sorted_list.copy()

    def sort_playlist(self):
        self.__song_list.sort()

    def binary_search(self, start, end, duration):
        if end >= start:
            middle = (start + end) // 2
            if self.__song_list[middle].get_duration() == duration:
                return middle
            elif self.__song_list[middle].get_duration() < duration:
                return self.binary_search(start, middle - 1, duration)
            else:
                return self.binary_search(middle + 1, end, duration)
        else:
            return -1

    def __repr__(self):
        rep = self.__name + " " + self.__purpose + " " + str(self.__length // 60) + " minutes" + "\n"
        rep2 = ""
        for song in self.__song_list:
            rep2 = rep2 + str(song)
        return rep + str(rep2)
