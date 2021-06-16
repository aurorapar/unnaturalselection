import os
import sys
from pathlib import Path

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

os.environ["KIVY_PROFILE_LANG"] = "1"

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["UNNATURAL_SELECTION_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__))
    os.environ["UNNATURAL_SELECTION_ROOT"] = str(Path(__file__).parent)

os.environ["UNNATURAL_SELECTION_ASSETS"] = os.path.join(
    os.environ["UNNATURAL_SELECTION_ROOT"], f"assets{os.sep}"
)


class LoadScreen(Screen):
    #lets do Database and Animation stuff here
    pass


class UnnaturalSelectionApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls.theme_style = "Dark"

    def build(self):
        return Builder.load_file(
            os.path.join(
                os.environ["UNNATURAL_SELECTION_ROOT"], 'main.kv'
            )
        )

    def change_screen(self, screen_name):
        self.root.current = screen_name

    def on_start(self):
        self.change_screen('title_screen')


app = UnnaturalSelectionApp()
app.run()
