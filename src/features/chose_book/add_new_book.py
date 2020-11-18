from src.book import Book
from src.database import Database
from src.console_app_framework.feature import Feature
from src.console_app_framework.input_processors.file_path_processor import FilePathProcessor


class AddNewBook(Feature):
    HELP = "Allows to add a new book"

    def run(self, interface, **kwargs):
        book_path = interface.get_input("Enter path to ebook", input_processor=FilePathProcessor())
        book = Book.from_path(book_path)

        db = Database()
        db.store_book(book)

        return book
