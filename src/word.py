from src.serialization.serializable import Serializable


class Word(Serializable):
    _STATIC_TYPE = "Word"
    _PROPERTIES_TO_SERIALIZE = {'stored_word', 'occurrences', 'is_known', 'is_checked'}

    def __init__(self, word=None):
        if word is not None:
            if len(word.split()) > 1:
                raise ValueError("Word class can store only single word strings")

        self.stored_word = word
        self.occurrences = 0
        self.is_known = False
        self.is_checked = False

    def mark_if_known(self, is_known):
        self.is_known = is_known
        self.is_checked = True

    def add_occurrence(self):
        self.occurrences += 1
