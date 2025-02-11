import time

import flet as ft
from blocks import Text
from download_song import youtube_dl
import threading
import re

class Downloading(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/downloading",
            horizontal_alignment="center",
        )
        from blocks import Divider, IconButton, TextButton, TextField
        self.title_text = Text("Downloading", size=30, weight="bold")
        self.page = page
        self.download_button = TextButton(Text("Click to Download", 20, "blue"), self.download)
        self.text_field = TextField("Paste the link here", self.download)
        self.back_btn = IconButton(ft.icons.ARROW_BACK, 1.5, action=self.toggle_playlist)
        self.controls = [
            ft.Row(
                [
                    self.back_btn,
                    ft.Container(expand=1),
                    self.title_text,
                    ft.Container(expand=1),
                    ft.Container(expand=1),
                ],
                alignment="start",
            ),
            ft.Column(
                [
                    Divider(height=20),
                    self.text_field,
                    Divider(height=20),
                    ft.Row(
                        [
                            self.download_button,
                        ],
                        alignment="center"
                    )
                ],
                alignment="center",
                expand=True,
            ),
        ]

    def toggle_playlist(self, event):
        self.page.session.clear()
        self.page.go("/playlist")

    def download(self, event):
        self.reset_fields()
        self.download_button.set_disabled(True)
        self.back_btn.set_disabled(True)
        self.back_btn.update()
        try:
            if not self.is_valid_link(self.text_field.get_value()):
                raise ValueError("Invalid link")
            self.download_button.set_text(Text("Downloading...", 20, "blue"))
            self.download_button.update()
            self.text_field.set_read_only(True)
            threading.Thread(target=self.download_audio).start()
        except ValueError:
            self.catch_error()

    def is_valid_link(self, link):
        return link != "" and (re.match(r'^(http://|https://)', link) is not None)

    def download_audio(self):
        try:
            youtube_dl(self.text_field.get_value())
            self.show_success_message()
        except Exception:
            self.catch_error()

    def reset_fields(self):
        self.download_button.set_text(Text("Click to Download", 20, "blue"))
        self.text_field.set_hint_text("Paste the link here")
        self.text_field.set_border_color("default")
        self.download_button.set_disabled(False)
        self.text_field.set_read_only(False)
        self.back_btn.set_disabled(False)
        self.download_button.update()
        self.text_field.update()
        self.back_btn.update()

    def catch_error(self):
        self.text_field.rm_value()
        self.download_button.set_text(Text("Click to Download", 20, "blue"))
        self.text_field.set_hint_text("Please enter a valid link or try again")
        self.text_field.set_border_color("red")
        self.download_button.set_disabled(False)
        self.text_field.set_read_only(False)
        self.back_btn.set_disabled(False)
        self.download_button.update()
        self.text_field.update()
        self.back_btn.update()

    def show_success_message(self):
        self.download_button.set_text(Text("Successful!", 20, "green"))
        self.download_button.update()
        time.sleep(3)
        self.reset_fields()
        self.text_field.rm_value()