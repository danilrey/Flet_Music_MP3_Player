import os

from song import Song


class SongLibrary:
    def __init__(self):
        self.playlist = []
        self.current_song = 0
        self.add_song()

    def add_song(self):
        for file in os.listdir("downloads"):
            if file.endswith(".mp3"):
                self.playlist.append(Song("downloads/" + file))

    def get_playlist(self):
        return self.playlist