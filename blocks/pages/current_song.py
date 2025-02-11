import flet as ft
from blocks import Text
from blocks.slider import Slider


class CurrentSong(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/song",
            padding=20,
            horizontal_alignment="center",
            vertical_alignment="center",
        )
        from blocks import Divider, IconButton
        self.slider = Slider("transparent",0.0,1.0,on_change=lambda e:self.toggle_seek(round(float(e.control.value))))
        self.audio = None
        self.page = page
        self.song = self.page.session.get("song")
        self.create_audio()
        self.duration = 0
        self.start = 0
        self.end = 0
        self.is_playing = False

        self.txt_start = Text(self.format_time(self.start))
        self.txt_end = Text(f"-{self.format_time(self.end)}")

        self.back_btn = IconButton(
            ft.icons.ARROW_BACK, 1.5, self.toggle_playlist
        )

        self.play_btn = self.create_toggle_button(
            ft.icons.PLAY_ARROW_ROUNDED,2,self.play
        )

        self.controls = [
            ft.Row(
                [self.back_btn],
                alignment="start"
            ),
            ft.Container(
                height=120,
                expand=True,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=6,
                    blur_radius=10,
                    color = ft.colors.with_opacity(0.35,"black")
                ),
                image_fit="cover",
                image_src=self.song.get_img_src()
            ),
            Divider(height=10),
            ft.Column(
                [
                    ft.Row(
                        controls=[Text(self.song.name(),18,weight="bold")]
                    ),
                    ft.Row(
                        controls=[Text(self.song.artist(),15,opacity=0.80)]
                    )
                ],
                spacing=1
            ),
            Divider(height=10),
            ft.Column(
                [
                    ft.Row([self.txt_start,self.txt_end],alignment="spaceBetween"),
                    self.slider
                ],
                spacing=0
            ),
            Divider(height=10),
            ft.Row(
                [
                    self.create_toggle_button(
                        ft.icons.REPLAY_5_SHARP,1.2, lambda e: self.update_position(-5000)
                    ),
                    self.play_btn,
                    self.create_toggle_button(
                        ft.icons.FORWARD_5_SHARP, 1.2, lambda e: self.update_position(5000)
                    ),
                ],
                alignment="spaceEvenly"
            ),
            Divider(height=10)
        ]

    def toggle_playlist(self,event):
        self.audio.pause()
        self.page.session.clear()
        self.page.go("/playlist")

    def create_toggle_button(self,icon, scale, action):
        from blocks import IconButton
        return IconButton(icon,scale, action)

    def play(self,event):
        self.toggle_play_pause(event)
        self.duration = self.audio.get_duration()
        self.end = self.duration
        self.slider.set_max(self.duration)

    def toggle_play_pause(self, event):
        if self.is_playing:
            self.play_btn.set_icon(ft.icons.PLAY_ARROW_ROUNDED)
            self.audio.pause()
        else:
            self.play_btn.set_icon(ft.icons.PAUSE_ROUNDED)
            try:
                self.audio.resume()
            except Exception:
                self.audio.play()
        self.is_playing = False if self.is_playing else True
        self.play_btn.update()

    def update_start_end(self):
        if self.start < 0:
            self.start = 0
        if self.end > self.duration:
            self.end = self.duration

    def update_position(self, delta):
        pos_change = 0
        self.update_start_end()
        if self.start > 0:
            if delta == 5000:
                pos_change = 5000
            elif delta == -5000:
                pos_change = -5000
            pos = self.start + pos_change
            self.audio.seek(pos)
            self.start += pos_change
            self.end -= pos_change

    def update_slider(self, delta):
        self.slider.set_value(delta)
        self.slider.update()

    def update_time(self):
        self.txt_start.value = self.format_time(self.start)
        self.txt_end.value = f"-{self.format_time(self.end)}"
        self.txt_start.update()
        self.txt_end.update()

    def format_time(self, time):
        milliseconds = time
        minutes, seconds = divmod(milliseconds / 1000,60)
        formatted = "{:02}:{:02}".format(int(minutes),int(seconds))
        return formatted

    def toggle_seek(self,delta):
        self.start = delta
        self.end = self.duration - delta
        self.audio.seek(self.start)
        self.update_slider(delta)

    def _update(self, delta):
        self.start += 1000
        self.end -= 1000
        self.update_slider(delta)
        self.update_time()

    def create_audio(self):
        self.audio = ft.Audio(self.song.get_src(), on_position_changed=lambda e: self._update(int(e.data)), volume=1.0)
        self.page.overlay.append(self.audio)
