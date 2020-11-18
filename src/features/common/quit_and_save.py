from src.database import Database
from src.features.feature import Feature


class QuitAndSave(Feature):
    HELP = "Quit and save"

    def run(self, interface, *, book, **kwargs):
        db = Database()
        db.store_book(book)
        exit(0)
