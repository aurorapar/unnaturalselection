from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder

password_helper = """
MDTextField:
    hint_text: "Enter Password"
    helper_text: "(or click on forgot forgot)"
    helper_text_mode: "persistent"
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint_x: None
    width: 300
"""

forgot_password_helper = """
MDRectangleFlatButton:
    text: "Forgot Password"
    pos_hint: {'center_x': .4, 'center_y': .4}
    theme_text_color: 'Custom'
    text_color: (100 / 255.0, 100 / 255.0, 100 / 255.0, .8)
"""


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):

        self.password_textfield = Builder.load_string(password_helper)
        self.forgot_password_button = Builder.load_string(forgot_password_helper)
        self.forgot_password_button.on_release = self.show_data

        self.add_widget(self.password_textfield)
        self.add_widget(self.forgot_password_button)

    def show_data(self):
        if len(self.password_textfield.text) < 1:
            return

        self.password_dialogue_close_button = MDFlatButton(
            text="Close",
            on_release=self.close_dialogue
        )

        self.password_dialogue = MDDialog(
            text=f"You Entered: {self.password_textfield.text}",
            buttons=[
                self.password_dialogue_close_button
            ]
        )
        self.password_dialogue.open()

    def close_dialogue(self, obj):
        self.password_dialogue.dismiss()

