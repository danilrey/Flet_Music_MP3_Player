import flet as ft
from flet.core.alignment import center

from blocks import Text, IconButton
from song import SongLibrary, Song


class PlayList(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/playlist",
            horizontal_alignment=center
        )
        self.page = page
        self.title = "Music Player App"
        self.library = SongLibrary()
        self.playlist = self.library.playlist
        self.controls = [
            ft.Row(
                [
                    Text("PLAYLIST", size=30),
                ],
                alignment="center"
            ),
            ft.Divider(height=10, color="transparent"),
        ]
        self.generate_playlist()

    def generate_playlist(self):
        for song in self.playlist:
            self.controls.append(
                self.generate_song_row(song.name(),song.artist(),song)
            )

        self.controls.append(
            ft.Row(
                [IconButton("Download", 2,action=self.toggle_download)],
                alignment="bottomCenter"
            )
        )

    def generate_song_row(self, song_name, artist_name, song: Song):
        return ft.Container(
            ft.Row(
                [
                    Text(song_name, size=20),
                    Text(artist_name, size=15),
                ],
                alignment="spaceBetween"
            ),
            data=song,
            padding=10,
            on_click=self.toggle_song
        )

    def toggle_song(self, event):
        self.page.session.set("song",event.control.data)
        self.page.go("/song")

    def toggle_download(self, event):
        self.page.go("/downloads")