import os

from src.epub_reader import EpubReader, Preprocessor

from src.serialization.serializable import Serializable


class Word(Serializable):
    _STATIC_TYPE = "Word"
    _PROPERTIES_TO_SERIALIZE = {'word', 'occurrences', 'is_known', 'is_checked'}

    def __init__(self, word=None):
        self.word = word
        self.occurrences = 0
        self.is_known = False
        self.is_checked = False

    def mark(self, is_known):
        self.is_known = is_known
        self.is_checked = True

    def add_occurence(self):
        self.occurrences += 1


class Book(Serializable):
    _STATIC_TYPE = "Book"
    _PROPERTIES_TO_SERIALIZE = {'name', 'words_list'}

    def __init__(self):
        pass

    @classmethod
    def from_path(cls, path):
        obj = cls()
        obj.name = obj._get_name(path)
        obj.words_list = obj._get_words_list(path)
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

            words_map[word].add_occurence()

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

