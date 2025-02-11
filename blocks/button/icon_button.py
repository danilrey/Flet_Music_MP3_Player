import flet as ft

class IconButton(ft.IconButton):
    def __init__(self, icon, scale, action):
        super().__init__()
        self.icon = icon
        self.scale = scale
        self.on_click = action
        self.hover_color = ft.colors.with_opacity(0.1, "blue")

    def set_icon(self, icon):
        self.icon = icon

    def click_action(self, action):
        self.on_click = action

    def set_padding(self, padding):
        self.padding = padding

    def set_scale(self, scale):
        self.scale = scale

    def set_disabled(self, disabled):
        self.disabled = disabled

    def set_icon(self, icon):
        self.icon = icon