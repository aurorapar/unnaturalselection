from utils import load_kv

from kivymd.uix.screen import Screen

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class PasswordDialogue(MDDialog):

    def on_open(self):
        print("opening")


class LoginScreen(Screen):

    def show_data(self):

        if len(self.ids.password_textfield.text) < 1:
            return

        self.dialogue = MDDialog(
            type = 'custom',
            title = "Forgot Password",
            buttons = [
                MDFlatButton(
                    text="OK"
                ),
                MDFlatButton(
                    text="Cancel",
                    on_release=self.dismiss
                )
            ]
        )
        self.dialogue.text = self.ids.password_textfield.text
        self.dialogue.open()

    def dismiss(self):
        self.dialogue.dismiss()

load_kv()

