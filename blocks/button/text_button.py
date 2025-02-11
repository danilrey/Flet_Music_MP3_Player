import flet as ft
from blocks import Text

class TextButton(ft.TextButton):
    def __init__(self, text: Text, on_click):
        super().__init__()
        self.content = text
        self.on_click = on_click

    def set_text(self, text):
        self.content = text

    def click_action(self, action):
        self.on_click = action

    def set_disabled(self, disabled):
        self.disabled = disabled