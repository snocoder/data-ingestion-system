import random
import string


class UniqueIDGenerator:
    DEFAULT_ID_LENGTH = 4
    CHARACTERS = string.ascii_uppercase + string.digits

    def __init__(self, id_length=DEFAULT_ID_LENGTH):
        self.id_length = id_length
        self._generated_ids = set()

    def _generate_id(self):
        return ''.join(random.choice(self.CHARACTERS) for _ in range(self.id_length))

    def _is_unique(self, new_id):
        return new_id not in self._generated_ids

    def generate_unique_id(self):
        while True:
            new_id = self._generate_id()
            if self._is_unique(new_id):
                self._generated_ids.add(new_id)
                return new_id
