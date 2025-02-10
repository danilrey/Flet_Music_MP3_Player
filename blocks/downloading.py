import flet as ft

class Downloading(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/downloading",
            horizontal_alignment="center"
        )

        self.page = page
