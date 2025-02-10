import flet as ft

class Slider(ft.Slider):
    def __init__(self,color, min_value =0.0,max_value = 1.0, on_change = None):
        super().__init__()
        self.min = min_value
        self.max = max_value
        self.color = color
        self.on_change = on_change
        self.overlay_color = ft.colors.with_opacity(0.1, "blue")