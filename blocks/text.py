import flet as ft
from blocks import *

class Text(ft.Text):
    def __init__(self, content, size: int = 20, color = "white", weight = "normal", opacity = 1):
        super().__init__(content)
        self.value = content
        self.size = size
        self.color = color
        self.weight = weight
        self.opacity = opacity

    def set_text(self, content):
        self.value = content

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def set_weight(self, weight):
        self.weight = weight