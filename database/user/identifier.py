import os
import uuid
import json


class Identifier:

    file = 'identifier.txt'

    def __init__(self):
        self.uuid = None
        self.load()

    def load(self):
        if not self.uuid:

            if not os.path.exists(Identifier.file):

                self.uuid = uuid.uuid4().int
                with open(Identifier.file, 'w') as f:
                    json.dump(self.uuid, f)

                assert self.uuid
                print("User created!")

            else:
                with open(Identifier.file, 'r') as f:
                    self.uuid = json.load(f)

                assert self.uuid
                print("User loaded!")

        if not self.uuid:
            raise RuntimeError("Failed to generate unique identifier")
