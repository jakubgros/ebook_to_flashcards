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

    def __init__(self):
        self.event_handler = EventHandler(self.input_to_feature)

    def run(self, interface, **kwargs):
        self.event_handler.process(interface, "help", input_to_feature=self.input_to_feature)

        while True:
            feature_str = interface.get_input("Your choice", input_validator=lambda answ: answ in self.input_to_feature)
            ret = self.event_handler.process(interface, feature_str, **kwargs)

            if ret is not None:
                return ret
