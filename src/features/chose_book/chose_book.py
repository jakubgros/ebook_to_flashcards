from src.event_handler import EventHandler
from src.features.chose_book.add_new_book import AddNewBook
from src.features.common.display_help import DisplayHelp
from src.features.feature import Feature
from src.features.chose_book.pick_book_from_database import PickBookFromDatabase
from src.features.common.quit import Quit


class ChoseBook(Feature):
    input_to_feature = {
        "show all": PickBookFromDatabase(),
        "add new": AddNewBook(),
        "quit": Quit(),
        "help": DisplayHelp(),
    }

    def run(self, interface, **kwargs):
        self.event_handler.process(interface, "help", input_to_feature=self.input_to_feature)
        self.run_event_loop(interface, **kwargs)
