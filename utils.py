import inspect
from os.path import extsep, exists, splitext

import phonenumbers
from kivy.lang import Builder


def load_kv():
    '''This magical function lookup module name, and load the kv file
    with the same name (in the same directory)
    https://gist.github.com/tshirtman/d8423695fe821440b65688b8dbd22b0c
    '''
    filename = inspect.currentframe().f_back.f_code.co_filename
    f = extsep.join((splitext(filename)[0], 'kv'))
    if exists(f) and f not in Builder.files:
        Builder.load_file(f)


def format_phonenumber(phone_number):
    try:
        if not phone_number.startswith('+'):
            if not phone_number.startswith('+1'):
                phone_number = f'+1{phone_number}'
            else:
                phone_number = f'+{phone_number}'

        if phonenumbers.is_valid_number(phonenumbers.parse(phone_number, None)):
            return phone_number
        return None
    except:
        return None
