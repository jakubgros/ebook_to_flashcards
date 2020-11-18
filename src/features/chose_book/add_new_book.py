import os

from src.book import Book
from src.database import Database
from src.features.feature import Feature


class AddNewBook(Feature):
    HELP = "Allows to add a new book"
    def run(self, interface, **kwargs):
        book_path = interface.get_input("Enter path to ebook", input_validator=lambda answ: os.path.isfile(answ))
        book = Book.from_path(book_path)

        db = Database()
        db.store_book(book)

        return book