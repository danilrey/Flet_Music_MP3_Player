import flet as ft

class Divider(ft.Divider):
    def __init__(self, height = 20, color = "transparent", expand = False):
        super().__init__()
        self.height = height
        self.color = color
        self.expand = expand

    def set_height(self, height):
        self.height = height

    def set_color(self, color):
        self.color = color

    def set_expand(self, expand):
        self.expand = expand