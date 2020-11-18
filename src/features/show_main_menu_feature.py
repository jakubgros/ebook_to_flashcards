from src.event_handler import EventHandler
from src.features.common.display_help import DisplayHelp
from src.features.feature import Feature
from src.features.interrogate_to_mark_known_words.interrogate_to_mark_known_words import InterrogateToMarkKnownWordsFeature
from src.features.make_flashcards import MakeFlashcards


class ShowMainMenuFeature(Feature):
    input_to_feature = {
        "1": InterrogateToMarkKnownWordsFeature(),
        "2": MakeFlashcards(),
        "help": DisplayHelp(),
    }

    def run(self, interface, **kwargs):
        self.event_handler.process(interface, "help", input_to_feature=ShowMainMenuFeature.input_to_feature)

        while True:
            feature_str = interface.get_input("your choice", input_validator=lambda answ: answ in self.input_to_feature)
            ShowMainMenuFeature.event_handler.process(interface, feature_str, input_to_feature=ShowMainMenuFeature.input_to_feature)
            #TODO jagros add validation to Feature class that everything that is needed by features is passed to process


