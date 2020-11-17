import os
from enum import Enum, auto

from src.book import Book
from src.database import Database
from src.event_handler import EventHandler
from src.event_translator import EventTranslator
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

    class EventTypes(Enum):
        QUIT = auto()
        HELP = auto()
        SHOW_ALL_BOOKS = auto()
        ADD_NEW_BOOK = auto()

    input_to_event_mapping = {
        "show all": (EventTypes.SHOW_ALL_BOOKS, "Allows to pick a book from database"),
        "add new": (EventTypes.ADD_NEW_BOOK, "Allows to add a new book"),
        "quit": (EventTypes.QUIT, "Quit and save"),
        "help": (EventTypes.HELP, "Displays all commands"),
    }

    event_to_feature_mapping = {
        EventTypes.ADD_NEW_BOOK: AddNewBook(),
        EventTypes.SHOW_ALL_BOOKS: PickBookFromDatabase(),
        EventTypes.HELP: DisplayHelp(),
        EventTypes.QUIT: Quit()
    }

    def __init__(self):
        self.event_handler = EventHandler(self.event_to_feature_mapping, self.input_to_event_mapping, self.EventTypes)

    def run(self, interface, **kwargs):
        self.event_handler.process(interface, self.EventTypes.HELP,
                                                  input_to_event_mapping=self.input_to_event_mapping)  # TODO jagros add validation to Feature class that everything that is needed by features is passed to process

        while True:
            event_translator = EventTranslator(self.input_to_event_mapping)
            event_str = interface.get_input("your choice", input_validator=event_translator.is_valid)
            event = event_translator.translate(event_str)
            ret = self.event_handler.process(interface, event, **kwargs)

            if ret is not None:
                return ret
