from src.features.chose_book.add_new_book import AddNewBook
from src.console_app_framework.feature import Feature
from src.features.chose_book.pick_book_from_database import PickBookFromDatabase


class ChoseBook(Feature):
    input_to_feature = {
        "show all": PickBookFromDatabase(),
        "add new": AddNewBook(),
    }

    def run(self, interface, **kwargs):
        ret = self.run_event_loop(interface, display_help=True, **kwargs)
        if ret is not None:
            return ret