from src.features.feature import Feature
from src.features.interrogate_to_mark_known_words.interrogate_to_mark_known_words import InterrogateToMarkKnownWordsFeature
from src.features.make_flashcards import MakeFlashcards


class ShowMainMenuFeature(Feature):
    input_to_feature = {
        "1": InterrogateToMarkKnownWordsFeature(),
        "2": MakeFlashcards(),
    }

    def run(self, interface, **kwargs):
        self.run_event_loop(interface, display_help=True, **kwargs)



