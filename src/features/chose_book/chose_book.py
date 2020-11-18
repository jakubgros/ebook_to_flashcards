from src.features.chose_book.add_new_book import AddNewBook
from src.features.feature import Feature
from src.features.chose_book.pick_book_from_database import PickBookFromDatabase
from src.features.common.quit import Quit


class ChoseBook(Feature):
    input_to_feature = {
        "show all": PickBookFromDatabase(),
        "add new": AddNewBook(),
    }

    def run(self, interface, **kwargs):

        self.event_handler.process(interface, "help")

        self.run_event_loop(interface, **kwargs)
