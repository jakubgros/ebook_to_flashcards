from pathlib import Path

from src.translator.translator import Translator
from src.iterator import Iterator


class UserInterface:
    ANSWER_KNOWN = "KNOWN"  # TODO jagros use enums instead
    ANSWER_UNKNOWN = "UNKNOWN"
    PREVIOUS = "PREVIOUS"
    NEXT = "NEXT"
    QUIT = "QUIT"
    NEXT_NOT_PROCESSED = "NEXT_NOT_PROCESSED"
    PREVIOUS_NOT_PROCESSED = "PREVIOUS_NOT_PROCESSED"
    HELP = "HELP"

    def get_event(self, event_prompt, inputs_mapping):
        while True:
            answ = input(event_prompt)

            if answ in inputs_mapping:
                return inputs_mapping[answ][0]

            print(">> Invalid input, try again")
            continue

    def get_enter_word_prompt(self, word, idx, size):
        progress = f"[{idx + 1}/{size}]"

        if not word.is_checked:
            status = "[?]"
        else:
            status = f"{'[y]' if word.is_known else '[n]'}"

        return f"{progress} {status} {word.word}: "

    def _display_info(self, information):
        print(information)

    def interrogate_to_mark_known_words(self, book):
        size = len(book.words_list)
        it = Iterator(book.words_list)

        input_to_event_mapping = {
            "q": (self.ANSWER_KNOWN, "Answer known"),
            "w": (self.ANSWER_UNKNOWN, "Answer unknown"),
            "back": (self.PREVIOUS, "Go back"),
            "fwd": (self.NEXT, "Go forward"),
            "quit": (self.QUIT, "Quit and save"),
            "fwd np": (self.NEXT_NOT_PROCESSED, "Go forward to next unprocessed word"),
            "back np": (self.PREVIOUS_NOT_PROCESSED, "Go back to previous unprocessed word"),
            "help": (self.HELP, "Displays all commands"),
        }

        while not book.are_all_words_processed():
            idx, word = it.get()

            event_prompt = self.get_enter_word_prompt(word, idx, size)
            event = self.get_event(event_prompt, input_to_event_mapping)

            if event == UserInterface.ANSWER_KNOWN:
                word.mark(True)
                it.next()

            elif event == UserInterface.ANSWER_UNKNOWN:
                word.mark(False)
                it.next()

            elif event == UserInterface.PREVIOUS:
                success = it.previous()
                if not success:
                    self._display_info("can't go back")

            elif event == UserInterface.NEXT:
                success = it.next()
                if not success:
                    self._display_info("can't go forward")

            elif event == UserInterface.NEXT_NOT_PROCESSED:
                success = it.next(lambda w: not w.is_checked)
                if not success:
                    self._display_info(
                        "Everything from current point till the end has been processed. Can't jump forward to next unprocessed word. ")

            elif event == UserInterface.PREVIOUS_NOT_PROCESSED:
                success = it.previous(lambda w: not w.is_checked)
                if not success:
                    self._display_info(
                        "Everything from current point till the beggining has been processed. Can't jump backward to prevuous unprocessed word. ")

            elif event == UserInterface.HELP:
                for command, (_, description) in self.input_to_event_mapping.items():
                    print(f"\t{command} = {description}")

            elif event == UserInterface.QUIT:
                return

            else:
                raise Exception("Invalid interface answer")

    def _any_word_needs_translation(self, list_of_words):
        needing_translation = [word for word in list_of_words if word.is_checked and not word.is_known]
        return any(not word.translations for word in needing_translation)

    def get_pick_translations_for_the_word_prompt(self, word, translations, idx, size):
        progress = f"[{idx + 1}/{size}]"
        status = f'[{word.translations}]' if word.translations else '[?]'
        header = f"{progress} {status} {word.word}: "

        body = ""
        for idx, translation in enumerate(translations):
            translated_word = ", ".join(translation.word)
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
        size = len(book.words_list)
        it = Iterator(book.words_list)

        input_to_event_mapping = {
            "q": (self.ANSWER_KNOWN, "Answer known"),
            "w": (self.ANSWER_UNKNOWN, "Answer unknown"),
            "back": (self.PREVIOUS, "Go back"),
            "fwd": (self.NEXT, "Go forward"),
            "quit": (self.QUIT, "Quit and save"),
            "fwd np": (self.NEXT_NOT_PROCESSED, "Go forward to next unprocessed word"),
            "back np": (self.PREVIOUS_NOT_PROCESSED, "Go back to previous unprocessed word"),
            "help": (self.HELP, "Displays all commands"),
        }

        translator = Translator()
        while self._any_word_needs_translation(book.words_list):
            idx, word = it.get()

            translations = translator.get_translation(word.word)
            event_prompt = self.get_pick_translations_for_the_word_prompt(word, translations, idx, size)
            event = self.get_event(event_prompt, input_to_event_mapping)

            if event == UserInterface.HELP:
                for command, (_, description) in self.input_to_event_mapping.items():
                    print(f"\t{command} = {description}")

            elif event == UserInterface.QUIT:
                return

            else:
                raise Exception("Invalid interface answer")

    def get_path_of_ebook_to_process(self):
        data = input("Enter path to ebook: ")
        return str(Path(data))
