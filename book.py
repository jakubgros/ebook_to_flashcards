import os

from epub_reader import EpubReader, Preprocessor
import json


class Word:
    def __init__(self, word):
        self.word = word
        self.occurrences = 0
        self.is_known = False
        self.is_checked = False

    def mark(self, is_known):
        self.is_known = is_known
        self.is_checked = True

    def add_occurence(self):
        self.occurrences += 1

class Book:

    def __init__(self, path):
        self.name = self._get_name(path)
        self.words_list = self._get_words_list(path)

    def are_all_words_processed(self):
        return all(word.is_checked for word in self.words_list)

    def _get_words_list(self, path):
        reader = EpubReader(path)
        txt = reader.get_text()
        txt = Preprocessor.process(txt)

        words_map = dict()
        for word in txt:
            if word not in words_map:
                words_map[word] = Word(word)

            words_map[word].add_occurence()

        as_list = list(words_map.values())
        as_list.sort(key=lambda elem: elem.occurrences, reverse=True)

        return as_list

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @classmethod
    def from_json(cls, json_data):
        obj = cls()
        obj.name = json_data["name"]
        obj.words_list = json_data["words_list"]

    @staticmethod
    def deserialize(input):
        loaded_data = json.loads(input)
        return Book.from_json(loaded_data)

    def _get_name(self, path):
        dir, file_name = os.path.split(path)
        return file_name

    @property
    def known_words(self):
        return [word for word in self.words_list if word.is_checked and word.is_known]

    @property
    def unknown_words(self):
        return [word for word in self.words_list if word.is_checked and not word.is_known]