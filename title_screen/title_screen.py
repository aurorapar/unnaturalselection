from utils import load_kv

from kivy.uix.screenmanager import Screen
from kivy.app import App


class TitleScreen(Screen):

    def on_touch_up(self, touch):

        app = App.get_running_app()
        app.change_screen('login_screen')


load_kv()
