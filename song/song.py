import os
import re

class Song:
    def __init__(self, src):
        self.src = src
        self.song_name, self.artist_name = self.divide_src(self.src)
        self.img_src = self.find_img_src()

    def divide_src(self, src):
        base_name = os.path.basename(src)
        name, _ = os.path.splitext(base_name)
        if len(name.split(" - ")) == 2:
            parts = name.split(" - ")
            artist_name, song_name = parts
        elif len(name.split(" — ")) == 2:
            parts = name.split(" — ")
            artist_name, song_name = parts
        elif len(name.split(" – ")) == 2:
            parts = name.split(" – ")
            artist_name, song_name = parts
        else:
            artist_name = "Unknown"
            song_name = name
        song_name = re.sub(r'\(.*?\)', '', song_name).strip()
        artist_name = re.sub(r'\(.*?\)', '', artist_name).strip()
        return song_name, artist_name

    def name(self):
        return self.song_name

    def find_img_src(self):
        basename = os.path.basename(self.src)
        name, _ = os.path.splitext(basename)
        img_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img')
        for file in os.listdir(img_dir):
            if name in file:
                self.img_src = os.path.join('assets', 'img', file)
                return self.img_src

    def artist(self):
        return self.artist_name

    def get_src(self):
        return self.src

    def get_img_src(self):
        return self.img_src