from src.database import Database
from src.features.feature import Feature


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