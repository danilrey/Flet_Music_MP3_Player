import flet as ft
from flet.core.border_radius import vertical

from blocks import Text, IconButton


class Downloading(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/downloading",
            horizontal_alignment="center",
        )

        self.page = page
        self.controls = [
            ft.Row(
                [
                    IconButton(ft.icons.ARROW_BACK, 1.5, action=self.toggle_playlist),
                    ft.Container(expand=1),
                    Text("Downloading", size=30, weight="bold"),
                    ft.Container(expand=1),
                ],
                alignment="spaceBetween",
                expand=True
            )
        ]


    def toggle_playlist(self, e):
        self.page.session.clear()
        self.page.go("/playlist")