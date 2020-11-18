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
        self.run_event_loop(interface, **kwargs)



