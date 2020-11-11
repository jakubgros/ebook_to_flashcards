from enum import Enum, auto
from pathlib import Path

from src.translator.translator import Translator
from src.iterator import Iterator
from dotmap import DotMap

class EventTypes(Enum):
    ANSWER_KNOWN = auto()
    ANSWER_UNKNOWN = auto()
    PREVIOUS = auto()
    NEXT = auto()
    QUIT = auto()
    NEXT_NOT_PROCESSED = auto()
    PREVIOUS_NOT_PROCESSED = auto()
    HELP = auto()


class Event:

    @classmethod
    def from_string(cls, str_val):
        type, mapping = cls._parse(str_val)
        return cls(type, mapping)

    def __init__(self, answ, mapping):
        self.type, self.description = None, None
        if answ in mapping:
            self.type, self.description = mapping[answ]

    def is_valid(self):
        return self.type is not None

    @staticmethod
    def _parse(value):

        """
        self.type = event_type
        self.attributes = attributes
        """


class Feature:
    def __init__(self, function, description):
        self.function = function
        self.description = description

    def run(self, data):
        self.function(data)

class EventHandler:
    def __init__(self, event_type_to_function_and_description):
        self.event_type_to_function_and_description = event_type_to_function_and_description

    def process(self, event, data):
        feature = self.event_type_to_function_and_description[event.type]
        feature.function(event, data)

class UserInterface:

    def get_event(self, event_prompt, inputs_mapping):
        while True:
            answ = input(event_prompt)
            event = Event(answ, inputs_mapping)
            if event.is_valid():
                return event

            print(">> Invalid input, try again")
            continue

    def get_enter_word_prompt(self, word, idx, size):
        progress = f"[{idx + 1}/{size}]"

        if not word.is_checked:
            status = "[?]"
        else:
            status = f"{'[y]' if word.is_known else '[n]'}"

        return f"{progress} {status} {word.stored_word}: "

    def _display_info(self, information):
        print(information)

    def _run_interface(self, input_to_event_mapping, event_handler, data, event_prompt_getter):

            event_prompt = event_prompt_getter(data)
            event = self.get_event(event_prompt, input_to_event_mapping)

            if event.type == EventTypes.HELP:
                for command, (_, description) in input_to_event_mapping.items():
                    print(f"\t{command} = {description}")
            elif event.type == EventTypes.QUIT:
                return True
            else:
                event_handler.process(event, data)

            return False

    def interrogate_to_mark_known_words(self, book):
        input_to_event_mapping = {
            "q": (EventTypes.ANSWER_KNOWN, "Answer known"),
            "w": (EventTypes.ANSWER_UNKNOWN, "Answer unknown"),
            "back": (EventTypes.PREVIOUS, "Go back"),
            "fwd": (EventTypes.NEXT, "Go forward"),
            "quit": (EventTypes.QUIT, "Quit and save"),
            "fwd np": (EventTypes.NEXT_NOT_PROCESSED, "Go forward to next unprocessed word"),
            "back np": (EventTypes.PREVIOUS_NOT_PROCESSED, "Go back to previous unprocessed word"),
            "help": (EventTypes.HELP, "Displays all commands"),
        }

        def ANSWER_KNOWN_func(event, data):
            data.stored_word.mark_if_known(True)
            data.it.next()

        def ANSWER_UNKNOWN_func(event, data):
            data.stored_word.mark_if_known(False)
            data.it.next()

        def PREVIOUS_func(event, data):
            success = data.it.previous()
            if not success:
                self._display_info("can't go back")

        def NEXT_func(event, data):
            success = data.it.next()
            if not success:
                self._display_info("can't go forward")

        def NEXT_NOT_PROCESSED_func(event, data):
            success = data.it.next(lambda w: not w.is_checked)
            if not success:
                self._display_info(
                    "Everything from current point till the end has been processed. Can't jump forward to next unprocessed word. ")

        def PREVIOUS_NOT_PROCESSED_func(event, data):
            success = data.it.previous(lambda w: not w.is_checked)
            if not success:
                self._display_info(
                    "Everything from current point till the beggining has been processed. Can't jump backward to prevuous unprocessed word. ")

        event_mapping = {
            EventTypes.ANSWER_KNOWN: Feature(ANSWER_KNOWN_func, "Answer known"),
            EventTypes.ANSWER_UNKNOWN: Feature(ANSWER_UNKNOWN_func, "Answer unknown"),
            EventTypes.PREVIOUS: Feature(PREVIOUS_func, "Go back"),
            EventTypes.NEXT: Feature(NEXT_func, "Go forward"),
            EventTypes.NEXT_NOT_PROCESSED: Feature(NEXT_NOT_PROCESSED_func, "Go forward to next unprocessed word"),
            EventTypes.PREVIOUS_NOT_PROCESSED: Feature(PREVIOUS_NOT_PROCESSED_func,
                                                       "Go back to previous unprocessed word"),
        }

        #TODO jagros implement the below
        event_prompt = self.get_enter_word_prompt
        event_handler = EventHandler(event_mapping)

        size = len(book.words)
        it = Iterator(book.words)

        def event_prompt_getter(data):
            return self.get_enter_word_prompt(data.stored_word, data.idx, data.size)

        while not book.are_all_words_processed():
            idx, word = it.get()
            data = DotMap()
            data.it = it
            data.idx = idx
            data.word = word
            data.size = len(it)
            quit_signal_returned = self._run_interface(input_to_event_mapping, event_handler, data, event_prompt_getter)
            if quit_signal_returned:
                return





    def _any_word_needs_translation(self, list_of_words):
        needing_translation = [word for word in list_of_words if word.is_checked and not word.is_known]
        return any(not word.translations for word in needing_translation)

    def get_pick_translations_for_the_word_prompt(self, word, translations, idx, size):
        progress = f"[{idx + 1}/{size}]"
        status = f'[{word.translations}]' if word.translations else '[?]'
        header = f"{progress} {status} {word.stored_word}: "

        body = ""
        for idx, translation in enumerate(translations):
            translated_word = ", ".join(translation.stored_word)
            meanings = ", ".join(translation.meaning)

            if translation.examples_and_its_translations:
                examples_with_its_translations = "\n\t" + "\n\t".join("".join(example) for example in translation.examples_and_its_translations)
            else:
                examples_with_its_translations = ""
            translation_choice = f"[{idx}] {translated_word} = {meanings}"
            translation_choice += f"{examples_with_its_translations}"
            body += '\n' + translation_choice

        translation_prompt = header + body + "\n enter comma separated choices: "
        return translation_prompt

    def make_flashcards(self, book):
        size = len(book.words)
        it = Iterator(book.words)

        input_to_event_mapping = {
            "q": (EventTypes.ANSWER_KNOWN, "Answer known"),
            "w": (EventTypes.ANSWER_UNKNOWN, "Answer unknown"),
            "back": (EventTypes.PREVIOUS, "Go back"),
            "fwd": (EventTypes.NEXT, "Go forward"),
            "quit": (EventTypes.QUIT, "Quit and save"),
            "fwd np": (EventTypes.NEXT_NOT_PROCESSED, "Go forward to next unprocessed word"),
            "back np": (EventTypes.PREVIOUS_NOT_PROCESSED, "Go back to previous unprocessed word"),
            "help": (EventTypes.HELP, "Displays all commands"),
        }

        translator = Translator()
        while self._any_word_needs_translation(book.words):
            idx, word = it.get()

            translations = translator.get_translation(word.stored_word)
            event_prompt = self.get_pick_translations_for_the_word_prompt(word, translations, idx, size)
            event = self.get_event(event_prompt, input_to_event_mapping)

            if event == EventTypes.HELP:
                for command, (_, description) in self.input_to_event_mapping.items():
                    print(f"\t{command} = {description}")

            elif event == UserInterface.QUIT:
                return

            else:
                raise Exception("Invalid interface answer")

    def get_path_of_ebook_to_process(self):
        data = input("Enter path to ebook: ")
        return str(Path(data))
