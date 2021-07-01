import requests

from definitions import REGISTER_URL, LOGIN_URL
from utils import load_kv, format_phonenumber
from database.user.identity import Identity

from kivymd.uix.screen import Screen

from kivy.app import App
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

failed_login_messages = {

}


class LoginScreen(Screen):

    def on_pre_enter(self, *args):
        if Identity.exists():
            user_uuid, phone_number = Identity.load()
            self.login(user_uuid, phone_number)

    def login(self, user_uuid, phone_number):
        resp = requests.post(LOGIN_URL, data={'user_uuid': user_uuid,
                                              'phone_number': phone_number}
                             )

        if resp.status_code in [200]:
            app = App.get_running_app()
            app.change_screen('game_screen')
        elif resp.status_code in [403]:
            self.dialog = MDDialog(
                text=resp.text,
                buttons=[
                    MDFlatButton(
                        text="Close", on_release=self.goto_next_screen
                    ),
                ],
            )
            self.dialog.open()
        else:
            self.show_failed_login_message(resp.status_code)

    def show_failed_login_message(self, status_code):
        print("failed login message")
        msg = 'Unknown login error.' if status_code not in failed_login_messages.keys() else \
            failed_login_messages[status_code]

        self.dialog = MDDialog(
            text=msg,
            buttons=[
                MDFlatButton(
                    text="Close", on_release=self.goto_previous_screen
                ),
            ],
        )
        self.dialog.open()

    def submit_phonenumber(self):

        if not format_phonenumber(self.ids.phonenumber_textfield.text):
            self.dialog = MDDialog(
                text="This is not a valid phone phone number (Needs to have area code)",
                buttons=[
                    MDFlatButton(
                        text="Close", on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()


        self.dialog = MDDialog(
            text="On the next screen, enter the code you received via text",
            buttons=[
                MDFlatButton(
                                text="Send Text", on_release=self.process
                            ),
            ],
        )
        self.dialog.open()

    def process(self, inst):
        self.dialog.dismiss()
        Identity.save(format_phonenumber(self.ids.phonenumber_textfield.text))
        user_uuid, phone_number = Identity.load()
        resp = requests.post(REGISTER_URL,
                             data={'phone_number': phone_number,
                                   'user_uuid': user_uuid
                                   }
                             )
        if resp.status_code == 200:
            self.goto_next_screen()
        if resp.status_code == 201:
            self.dialog = MDDialog(
                text=resp.text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.goto_next_screen
                    )
                ]

            )
            self.dialog.open()
        if resp.status_code not in [200, 201]:
            self.dialog = MDDialog(
                text=resp.text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    )
                ]

            )
            self.dialog.open()

    def close_dialog(self, inst):
        self.dialog.dismiss()

    def goto_next_screen(self, inst=None):
        self.close_dialog(inst)
        app = App.get_running_app()
        app.change_screen('otp_screen')

    def goto_previous_screen(self, inst=None):
        self.close_dialog(inst)
        app = App.get_running_app()
        app.change_screen('title_screen')


load_kv()
