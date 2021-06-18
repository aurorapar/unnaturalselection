from utils import load_kv

from kivyauth.google_auth import initialize_google, login_google, logout_google
from kivyauth.utils import login_providers

from kivymd.uix.screen import Screen

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# don't store this client side. Use a webproxy to facilitate auth
GOOGLE_CLIENT_ID = 'REMOVED'
GOOGLE_SECRET = 'REMOVED'


class PasswordDialogue(MDDialog):

    def on_open(self):
        print("opening")


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        initialize_google(self.after_login,
                          self.error_listener,
                          GOOGLE_CLIENT_ID,
                          GOOGLE_SECRET
                          )

    def start_google_login(self):
        login_google()
        self.current_provider = login_providers.google

    def after_login(self, name, email, photo_url):
        self.dialogue = MDDialog(
            type='custom',
            title="Login Successful",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.dismiss
                )
            ]
        )
        self.dialogue.text = f"You have logged in with your Google Account\n{email}"
        self.dialogue.open()

    def error_listener(self):
        pass

    def dismiss(self, widget):
        self.dialogue.dismiss(force=True)

load_kv()

