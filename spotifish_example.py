from amnon_graphics import AmnonApp, AmnonButton, layouts, colors, AmnonLabel


class SpotifishApp:
    def __init__(self):
        self.app = AmnonApp(
            name='Spotifish',
            height=800,
            width=1400
        )
        self.add_play_song_buttons()
        self.add_title()

    def play_song(self, song_name):
        """This would need to actually play the song using subprocess"""
        print(song_name)

    def add_title(self):
        title = AmnonLabel(
            position=layouts.Position(700, 20),
            size=layouts.Size(200, 50),
            text='Spotifish',
            font_size=30
        )
        self.app.add_label(title)

    def add_play_song_buttons(self):
        for i, song_name in enumerate(('song1', 'song2', 'song3')):
            song_button = AmnonButton(
                position=layouts.Position(20, i * 50),
                size=layouts.Size(120, 40),
                on_click=self.play_song,
                on_click_params=[song_name],
                text=f'Play "{song_name}"',
                background_color=colors.GRAY
            )
            self.app.add_button(song_button)

    def run(self):
        self.app.run()


if __name__ == '__main__':
    spotifish = SpotifishApp()
    spotifish.run()
