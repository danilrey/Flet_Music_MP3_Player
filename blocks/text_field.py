
import flet as ft

class TextField(ft.TextField):
    def __init__(self, hint_text, on_enter):
        super().__init__()
        self.on_enter = on_enter
        self.hint_text = hint_text
        self.border_radius = 50

    def set_border_radius(self, radius: int):
        self.border_radius = radius
        self.update()

    def set_hint_text(self, text: str):
        self.hint_text = text
        self.update()

    def set_border_color(self, color: str):
        self.border_color = color
        self.update()

    def set_read_only(self, read_only):
        self.read_only = read_only
        self.update()

    def rm_value(self):
        self.value = ""
        self.update()

    def on_enter(self, func):
        self.on_enter = func
        self.update()

    def get_value(self):
        return self.value