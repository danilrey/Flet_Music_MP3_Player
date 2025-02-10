import os


class Song:
    def __init__(self, src):
        self.src = src
        self.song_name, self.artist_name = self.divide_src(self.src)
        self.img_src = "img/image.png"

    def divide_src(self, src):
        base_name = os.path.basename(src)
        name, _ = os.path.splitext(base_name)
        parts = name.split(" - ")
        if len(parts) == 2:
            artist_name, song_name = parts
        else:
            artist_name = "Unknown"
            song_name = parts[0]
        return song_name, artist_name

    def name(self):
        return self.song_name

    def artist(self):
        return self.artist_name

    def src(self):
        return self.src