import os
from enum import Enum, auto

from src.book import Book
from src.database import Database
from src.event_handler import EventHandler
from src.features.displayhelp import DisplayHelp
from src.features.feature import Feature

class AddNewBook(Feature):
    def run(self, interface, **kwargs):
        book_path = interface.get_input("Enter path to ebook", input_validator=lambda answ: os.path.isfile(answ))
        book = Book.from_path(book_path)

        db = Database()
        db.store_book(book)

        return book

class Quit(Feature):
    def run(self, interface, **kwargs):
       exit(0)

class PickBookFromDatabase(Feature):
    def run(self, interface, **kwargs):
        db = Database()

        all_stored_books = db.get_all_stored_books()
        if not all_stored_books:
            interface.display_info(f"There are no books in database")
            return None

        for idx, book in enumerate(all_stored_books):
            interface.display_info(f"[{idx}] {book.name}")

        def is_answer_valid(answ):
            try:
                int_answ = int(answ)
                if 0 < int_answ < len(all_stored_books):
                    return True
            except:
                pass
            return False

        choice = interface.get_input("Your choice", input_validator=is_answer_valid)

        return all_stored_books[choice]

class ChoseBook(Feature):
    input_to_feature = {
        "show all": (PickBookFromDatabase(), "Allows to pick a book from database"),
        "add new": (AddNewBook(), "Allows to add a new book"),
        "quit": (Quit(), "Quit and save"),
        "help": (DisplayHelp(), "Displays all commands"),
    }

    def __init__(self):
        self.event_handler = EventHandler(self.input_to_feature)

    def run(self, interface, **kwargs):
        self.event_handler.process(interface, "help", input_to_feature=self.input_to_feature)

        while True:
            feature_str = interface.get_input("your choice", input_validator=lambda answ: answ in self.input_to_feature)
            ret = self.event_handler.process(interface, feature_str, **kwargs)

            if ret is not None:
                return ret
