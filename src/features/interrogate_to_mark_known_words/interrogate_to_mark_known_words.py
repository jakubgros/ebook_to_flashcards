from src.database import Database
from src.event_handler import EventHandler
from src.features.chose_book.chose_book import ChoseBook
from src.features.common.display_help import DisplayHelp
from src.features.feature import Feature
from src.features.interrogate_to_mark_known_words.go_to_next import GoToNext
from src.features.interrogate_to_mark_known_words.go_to_next_not_processed import GoToNextNotProcessed
from src.features.interrogate_to_mark_known_words.go_to_previous import GoToPrevious
from src.features.interrogate_to_mark_known_words.go_to_previous_not_processed import GoToPreviousNotProcessed
from src.features.interrogate_to_mark_known_words.mark_known_answer import MarkKnownAnswer
from src.features.interrogate_to_mark_known_words.mark_unknown_answer import MarkUnknownAnswer
from src.features.common.quit_and_save import QuitAndSave
from src.iterator import Iterator


class InterrogateToMarkKnownWordsFeature(Feature):
    HELP = "Allows you to process a book in order to mark known words"

    input_to_feature = {
        "q": MarkKnownAnswer(),
        "w": MarkUnknownAnswer(),
        "back": GoToPrevious(),
        "fwd": GoToNext(),
        "quit": QuitAndSave(),
        "fwd np": GoToNextNotProcessed(),
        "back np": GoToPreviousNotProcessed(),
        "help": DisplayHelp(),
    }

    def run(self, interface, **kwargs):
        book = ChoseBook().run(interface, **kwargs)

        it = Iterator(book.words)
        try:
            while not book.are_all_words_processed():
                idx, word = it.get()

                event_prompt = self._get_enter_word_prompt(word, idx, len(it))
                feature_str = interface.get_input(event_prompt, input_validator=lambda answ: answ in self.input_to_feature)
                ret = self.event_handler.process(interface, feature_str, it=it, idx=idx, word=word, size=len(it), book=book)
        finally:
            db = Database()
            db.store_book(book)


    def _get_enter_word_prompt(self, word, idx, size):
        progress = f"[{idx + 1}/{size}]"

        if not word.is_checked:
            status = "[?]"
        else:
            status = f"{'[y]' if word.is_known else '[n]'}"

        return f"{progress} {status} {word.stored_word}"


