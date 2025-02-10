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
                    Text("Your Playlist:", size=30, weight="bold"),
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
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Divider(height=20, color="transparent"),
                            IconButton(ft.icons.DOWNLOAD, 2, action=self.toggle_download),
                        ],
                        alignment="center"
                    ),
                    ft.Divider(height=20, color="transparent"),
                ],
                alignment="end",
                expand=True,
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
            on_click=self.toggle_song,
            on_hover=lambda e: self.highlight_on_hover(e)
        )

    def highlight_on_hover(self, event):
        if event.data == "true":
            event.control.bgcolor = ft.colors.with_opacity(0.1, "blue")
        else:
            event.control.bgcolor = None
        event.control.update()

    def toggle_song(self, event):
        self.page.session.set("song",event.control.data)
        self.page.go("/song")

    def toggle_download(self, event):
        self.page.session.clear()
        self.page.go("/downloads")