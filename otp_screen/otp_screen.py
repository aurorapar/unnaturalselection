import requests

from database.user.identity import Identity
from definitions import VERIFY_URL
from utils import load_kv

from kivy.app import App

from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class OTPScreen(Screen):

    def submit_code(self):
        uuid, _ = Identity.load()
        otp = self.ids.otp_textfield.text
        resp = requests.post(VERIFY_URL, data={'otp': otp, 'user_uuid': uuid})
        if resp.status_code not in [200]:
            self.dialog = MDDialog (
                text=resp.text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    )
                ]

            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                text=resp.text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.goto_next_screen
                    )
                ]

            )

            self.dialog.open()

    def close_dialog(self, inst):
        self.dialog.dismiss()

    def goto_next_screen(self, inst):
        self.close_dialog(inst)
        app = App.get_running_app()
        app.change_screen('game_screen')

load_kv()
