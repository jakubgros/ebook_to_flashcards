import unittest

from src.book import Book
from src.database import Database
from src.translator.translator import Translator
from src.user_interface import UserInterface


class FlashcardsMakerTest(unittest.TestCase):
    def test_something(self): #TODO jagros remove

        db = Database()
        ui = UserInterface()

        book_path = r"C:\Users\jakub\Desktop\read_new_words_collector\book.epub"
        book = Book.from_path(book_path)

        if db.has_book(book):
            book = db.restore_book(book)

        known_words = db.get_known_words()
        book.mark_known_words(known_words)

        ui.make_flashcards(book)

if __name__ == '__main__':
    unittest.main()
