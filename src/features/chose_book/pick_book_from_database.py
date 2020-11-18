from src.database import Database
from src.features.feature import Feature
from src.input_processors.int_range_validator import IntInRangeInputProcessor


class PickBookFromDatabase(Feature):
    HELP = "Allows to pick a book from database"

    def run(self, interface, **kwargs):
        db = Database()
        all_stored_books = db.get_all_stored_books()

        if not all_stored_books:
            interface.display_info(f"There are no books in database")
            return None

        for idx, book in enumerate(all_stored_books):
            interface.display_info(f"[{idx}] {book.name}")

        choice = interface.get_input("Your choice", input_processor=IntInRangeInputProcessor(valid_range=(0, len(all_stored_books))))
        return all_stored_books[choice]
