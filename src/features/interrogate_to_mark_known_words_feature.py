from src.database import Database
from src.event_handler import EventHandler
from src.features.chose_book import ChoseBook
from src.features.displayhelp import DisplayHelp
from src.features.feature import Feature
from src.iterator import Iterator


class QuitAndSave(Feature):
    def run(self, interface, *, book, **kwargs):
        db = Database()
        db.store_book(book)
        exit(0)


class ANSWER_KNOWN_feat(Feature):
    def run(self, interface, *, word, it, **kwargs):
        word.mark_if_known(True)
        it.next()

class ANSWER_UNKNOWN_feat(Feature):
    def run(self, interface, *, word, it, **kwargs):
        word.mark_if_known(False)
        it.next()

class PREVIOUS_feat(Feature):
    def run(self, interface, *, it, **kwargs):
        success = it.previous()
        if not success:
            interface.display_info("can't go back")

class NEXT_feat(Feature):
    def run(self, interface, *, it, **kwargs):
        success = it.next()
        if not success:
            interface.display_info("can't go forward")

class NEXT_NOT_PROCESSED_feat(Feature):
    def run(self, interface, *, it, **kwargs):
        success = it.next(lambda w: not w.is_checked)
        if not success:
            interface.display_info("Everything from current point till the end has been processed. Can't jump forward to next unprocessed word. ")

class PREVIOUS_NOT_PROCESSED_feat(Feature):
    def run(self, interface, *, it, **kwargs):
        success = it.previous(lambda w: not w.is_checked)
        if not success:
            interface.display_info("Everything from current point till the beggining has been processed. Can't jump backward to prevuous unprocessed word. ")



class InterrogateToMarkKnownWordsFeature(Feature):
    input_to_feature = {
        "q": (ANSWER_KNOWN_feat(), "Answer known"),
        "w": (ANSWER_UNKNOWN_feat(), "Answer unknown"),
        "back": (PREVIOUS_feat(), "Go back"),
        "fwd": (NEXT_feat(), "Go forward"),
        "quit": (QuitAndSave(), "Quit and save"),
        "fwd np": (NEXT_NOT_PROCESSED_feat(), "Go forward to next unprocessed word"),
        "back np": (PREVIOUS_NOT_PROCESSED_feat(), "Go back to previous unprocessed word"),
        "help": (DisplayHelp(), "Displays all commands"),
    }

    def __init__(self):
        self.event_handler = EventHandler(self.input_to_feature)

    def run(self, interface, **kwargs):
        book = ChoseBook().run(interface, **kwargs)

        it = Iterator(book.words)
        try:
            while not book.are_all_words_processed():
                idx, word = it.get()

                event_prompt = self._get_enter_word_prompt(word, idx, len(it))
                feature_str = interface.get_input(event_prompt, input_validator=lambda answ: answ in self.input_to_feature)
                ret = self.event_handler.process(interface,
                                                 feature_str, it=it, idx=idx, word=word,
                                                 size=len(it), input_to_event_mapping=self.input_to_event_mapping,
                                                 book=book)
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


