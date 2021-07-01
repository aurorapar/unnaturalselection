import os
import uuid
import json

import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
parentdir = os.path.dirname(parentdir)
parentdir = os.path.dirname(parentdir)
sys.path.append(parentdir)

from definitions import IDENTITY_FILE


class Identity:
    file = IDENTITY_FILE

    @staticmethod
    def save(phone_number):
        if Identity.exists():
            raise RuntimeError('Identity already exists')
        with open(Identity.file, 'w') as f:
            ids = [str(uuid.uuid4()), phone_number]
            json.dump(ids, f)
        return Identity.load()

    @staticmethod
    def load():
        if not Identity.exists():
            raise RuntimeError('Identity doesn\'t Exist!')
        with open(Identity.file, 'r') as f:
            user_uuid, phone_number = json.load(f)

        assert user_uuid
        assert phone_number

        return user_uuid, phone_number

    @staticmethod
    def delete():
        if os.path.exists(Identity.file):
            os.remove(Identity.file)

    @staticmethod
    def exists():
        return os.path.exists(Identity.file)