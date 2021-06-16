import time

from kivy.uix.screenmanager import Screen


class TitleScreen(Screen):

    def build(self):
        self.root.theme_cls.primary_palette = "Dark"

        self.start_time = time.time()
        # change this to a DB call
        self.load_time = 5

    def on_touch_up(self, touch):
        if time.time() - self.start_time > self.load_time:
            # Can Change Screen Now
            pass
