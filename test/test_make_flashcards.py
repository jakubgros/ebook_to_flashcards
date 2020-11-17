import unittest

from src.book import Book
from src.env_utils.base_dir import base_dir
from src.features.make_flashcards import MakeFlashcards
from src.translator.translator import Translator
from src.user_interface import Interface


class MyTestCase(unittest.TestCase):
    def test_something(self):
        feature = MakeFlashcards()
        interface = Interface()
        book = Book.from_path(f"{base_dir}\\test\\data\\short_book.epub")

        for word in book.words:
            word.mark_if_known(False)

        feature.run(interface, book)




if __name__ == '__main__':
    unittest.main()
