from enum import Enum, auto

from src.event_handler import EventHandler
from src.event_translator import EventTranslator
from src.features import display_help
from src.features.feature import Feature
from src.features.interrogate_to_mark_known_words_feature import InterrogateToMarkKnownWordsFeature
from src.features.make_flashcards import MakeFlashcards


class ShowMainMenuFeature(Feature):
    class EventTypes(Enum):
        INTERROGATE_TO_MARK_KNOWN_WORDS = auto()
        MAKE_FLASHCARDS = auto()
        DISPLAY_HELP = auto()

    input_to_event_mapping = {
        "1": (EventTypes.INTERROGATE_TO_MARK_KNOWN_WORDS, "Allows you to process a book in order to mark known words"),
        "2": (EventTypes.MAKE_FLASHCARDS, "Allows to make a flashcards from unknown words from a book"),
        "help": (EventTypes.DISPLAY_HELP, "Displays help")
    }


    event_to_feature_mapping = {
        EventTypes.INTERROGATE_TO_MARK_KNOWN_WORDS: InterrogateToMarkKnownWordsFeature(),
        EventTypes.MAKE_FLASHCARDS: MakeFlashcards(),
        EventTypes.DISPLAY_HELP: display_help(),
    }

    event_handler = EventHandler(event_to_feature_mapping, input_to_event_mapping, EventTypes)

    @staticmethod
    def run(interface, **kwargs):

        while True:
            ShowMainMenuFeature.event_handler.process(interface, ShowMainMenuFeature.EventTypes.DISPLAY_HELP, input_to_event_mapping=ShowMainMenuFeature.input_to_event_mapping)     #TODO jagros add validation to Feature class that everything that is needed by features is passed to process

            event_translator = EventTranslator(ShowMainMenuFeature.input_to_event_mapping)
            event_str = interface.get_input("your choice", input_validator=event_translator.is_valid)
            event = event_translator.translate(event_str)

            ShowMainMenuFeature.event_handler.process(interface, event, input_to_event_mapping=ShowMainMenuFeature.input_to_event_mapping)     #TODO jagros add validation to Feature class that everything that is needed by features is passed to process


