from utils import load_kv

from kivymd.uix.screen import Screen

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class PasswordDialogue(MDDialog):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_release = self.dismiss
        self.name = "password_dialogue",
        self.buttons = [
            MDFlatButton(
                text="OK"
            ),
            MDFlatButton(
                text="Close",
                on_release=self.dismiss
            )
        ]


class LoginScreen(Screen):

    def show_data(self):

        if len(self.ids.password_textfield.text) < 1:
            return

        dialogue = PasswordDialogue()
        dialogue.text = self.ids.password_textfield.text
        dialogue.open()

load_kv()

