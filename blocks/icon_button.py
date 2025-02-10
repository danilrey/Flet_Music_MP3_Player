import flet as ft

class IconButton(ft.IconButton):
    def __init__(self, icon, scale, action):
        super().__init__()
        self.icon = icon
        self.scale = scale
        self.on_click = action

    def set_icon(self, icon):
        self.icon = icon

    def click_action(self, action):
        self.on_click = action