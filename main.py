import os
import sys
from pathlib import Path

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from libs.baseclass.title_screen import TitleScreen

os.environ["KIVY_PROFILE_LANG"] = "1"

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["UNNATURAL_SELECTION_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__))
    os.environ["UNNATURAL_SELECTION_ROOT"] = str(Path(__file__).parent)
    # os.environ["KITCHEN_SINK_ROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ["UNNATURAL_SELECTION_ASSETS"] = os.path.join(
    os.environ["UNNATURAL_SELECTION_ROOT"], f"assets{os.sep}"
)

screen_helper = """
ScreenManager:
    TitleScreen:        
    LoginScreen:
    

        
<LoginScreen>:
    name: 'login_screen'    
"""


class UnnaturalSelectionApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen_manager = ScreenManager()

    def build(self):
        Builder.load_file(
            os.path.join(
                os.environ["UNNATURAL_SELECTION_ROOT"], "libs", "kv", "title_screen.kv"
            )
        )
        return TitleScreen()

    def change_screen(self, screen_name):
        if not self.screen_manager.has_screen(screen_name):
            Builder.load_file(
                os.path.join(
                    os.environ["UNNATURAL_SELECTION_ROOT"], "libs", "kv", f"{screen_name}.kv"
                )
            )

        self.screen_manager.current = screen_name


UnnaturalSelectionApp().run()

