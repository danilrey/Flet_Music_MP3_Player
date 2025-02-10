
import flet as ft

from blocks import PlayList, Downloading
from song import CurrentSong


def main(page: ft.Page):
    page.title = "Music Player App"
    page.window.width = 400
    page.window.height = 700
    page.window.resizable = False

    def router(route):
        page.views.clear()

        if page.route == "/playlist":
            playlist = PlayList(page)
            page.views.append(playlist)

        if page.route == "/song":
            song = CurrentSong(page)
            page.views.append(song)

        if page.route == "/downloads":
            downloads = Downloading(page)
            page.views.append(downloads)


        page.update()

    page.on_route_change = router
    page.go("/playlist")

ft.app(target=main, assets_dir="downloads")
