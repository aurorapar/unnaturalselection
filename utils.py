import inspect
from os.path import extsep, exists, splitext

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
