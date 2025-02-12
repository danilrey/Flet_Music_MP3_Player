import flet as ft
from flet.core.alignment import center

from blocks import Text
from song import SongLibrary, Song


class PlayList(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/playlist",
            horizontal_alignment=center
        )
        from blocks import Divider
        self.page = page
        self.title = "Music Player App"
        self.library = SongLibrary()
        self.playlist = self.library.get_playlist()
        self.controls = [
            ft.Row(
                [
                    Text("Your Playlist:", size=30, weight="bold"),
                ],
                alignment="center"
            ),
            Divider(height=10),
            ft.Column(
                controls=[],
                scroll="auto",
                expand=True
            ),
            ft.Row(
                [
                    Divider(),
                    ft.IconButton(icon=ft.Icons.DOWNLOAD, scale=2, on_click=self.toggle_download),
                ],
                alignment="center"
            ),
            Divider(),
        ]
        self.generate_playlist()

    def generate_playlist(self):
        playlist_column = self.controls[2]
        for song in self.playlist:
            playlist_column.controls.append(
                self.generate_song_row(song.name(), song.artist(), song)
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
            event.control.bgcolor = ft.Colors.with_opacity(0.1, "blue")
        else:
            event.control.bgcolor = None
        event.control.update()

    def toggle_song(self, event):
        self.page.session.set("song", event.control.data)
        self.page.go("/song")

    def toggle_download(self, event):
        self.page.session.clear()
        self.page.go("/assets")