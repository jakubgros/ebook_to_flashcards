import os

from src.epub_reader import EpubReader, Preprocessor

from src.serialization.serializable import Serializable
from src.word import Word


class Book(Serializable):
    _STATIC_TYPE = "Book"
    _PROPERTIES_TO_SERIALIZE = {'name', 'words_list', 'path', 'meaning'}

    def __init__(self):
        pass

    @classmethod
    def from_path(cls, path):
        obj = cls()
        obj.path = path
        obj.name = obj._get_name(path)
        obj.words_list = obj._get_words_list(path)
        obj.meaning = []
        return obj

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

            words_map[word].add_occurrence()

        as_list = list(words_map.values())
        as_list.sort(key=lambda elem: elem.occurrences, reverse=True)

        return as_list

    def _get_name(self, path):
        dir, file_name = os.path.split(path)
        return file_name

    @property
    def known_words(self):
        return [word for word in self.words_list if word.is_checked and word.is_known]

    @property
    def unknown_words(self):
        return [word for word in self.words_list if word.is_checked and not word.is_known]

    def mark_known_words(self, known_words):
        for word in self.words_list:
            if word.word in known_words:
                word.mark(True)

