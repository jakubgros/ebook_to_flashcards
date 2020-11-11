import os

from src.epub_reader import EpubReader
from src.preprocessor import Preprocessor

from src.serialization.serializable import Serializable
from src.word import Word


class Book(Serializable):
    _STATIC_TYPE = "Book"
    _PROPERTIES_TO_SERIALIZE = {'name', 'words', 'path', 'meaning'}

    @classmethod
    def from_path(cls, path):
        book = cls()
        book.path = path
        book.name = book._get_file_name(path)
        book.words = book._get_words(path)
        book.meaning = []
        return book

    def are_all_words_processed(self):
        return all(word.is_checked for word in self.words)

    @property
    def known_words(self):
        return {word for word in self.words if word.is_checked and word.is_known}

    @property
    def unknown_words(self):
        return {word for word in self.words if word.is_checked and not word.is_known}

    @staticmethod
    def _get_words(path):
        reader = EpubReader(path)
        book_text = reader.get_text()
        book_text = Preprocessor.process(book_text)

        words_to_occurrences = dict()
        for word in book_text:
            if word not in words_to_occurrences:
                words_to_occurrences[word] = Word(word)

            words_to_occurrences[word].add_occurrence()

        words_and_occurrences = list(words_to_occurrences.values())
        words_and_occurrences.sort(key=lambda elem: elem.occurrences, reverse=True)

        return words_and_occurrences

    @staticmethod
    def _get_file_name(path):
        _, file_name = os.path.split(path)
        return file_name
