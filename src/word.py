from src.serialization.serializable import Serializable


class Word(Serializable):
    _STATIC_TYPE = "Word"
    _PROPERTIES_TO_SERIALIZE = {'word', 'occurrences', 'is_known', 'is_checked', 'translations'} #TODO change to serialize everything by default and add list of fields that shouldn't be serialized, because now it's easy to forget to add the new field to the list

    def __init__(self, word=None):
        self.word = word
        self.occurrences = 0
        self.is_known = False
        self.is_checked = False
        self.translations = []

    def mark(self, is_known):
        self.is_known = is_known
        self.is_checked = True

    def add_occurence(self):
        self.occurrences += 1

    def add_translation(self, translation):
        self.translations.append(translation)