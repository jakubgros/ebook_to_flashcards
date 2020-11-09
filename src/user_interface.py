from pathlib import Path

from src.iterator import Iterator


class UserInterface:
    ANSWER_KNOWN = "KNOWN" #TODO jagros use enums instead
    ANSWER_UNKNOWN = "UNKNOWN"
    PREVIOUS = "PREVIOUS"
    NEXT = "NEXT"
    QUIT = "QUIT"
    NEXT_NOT_PROCESSED = "NEXT_NOT_PROCESSED"
    PREVIOUS_NOT_PROCESSED = "PREVIOUS_NOT_PROCESSED"
    HELP = "HELP"

    input_to_event_mapping = {
        "q": (ANSWER_KNOWN, "Answer known"),
        "w": (ANSWER_UNKNOWN, "Answer unknown"),
        "back": (PREVIOUS, "Go back"),
        "fwd": (NEXT, "Go forward"),
        "quit": (QUIT, "Quit and save"),
        "fwd np": (NEXT_NOT_PROCESSED, "Go forward to next unprocessed word"),
        "back np": (PREVIOUS_NOT_PROCESSED, "Go back to previous unprocessed word"),
        "help": (HELP, "Displays all commands"),
    }

    def get_event(self, event_prompt):
        while True:
            answ = input(event_prompt)

            if answ in self.input_to_event_mapping:
                return self.input_to_event_mapping[answ][0]

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

    def process(self, book):
        size = len(book.words_list)
        it = Iterator(book.words_list)

        while not book.are_all_words_processed():
            idx, word = it.get()

            event_prompt = self.get_enter_word_prompt(word, idx, size)
            event = self.get_event(event_prompt)

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
                    self._display_info("Everything from current point till the end has been processed. Can't jump forward to next unprocessed word. ")

            elif event == UserInterface.PREVIOUS_NOT_PROCESSED:
                success = it.previous(lambda w: not w.is_checked)
                if not success:
                    self._display_info("Everything from current point till the beggining has been processed. Can't jump backward to prevuous unprocessed word. ")

            elif event == UserInterface.HELP:
                for command, (_, description) in self.input_to_event_mapping.items():
                    print(f"\t{command} = {description}")

            elif event == UserInterface.QUIT:
                return

            else:
                raise Exception("Invalid interface answer")

    def get_path_of_ebook_to_process(self):
        data = input("Enter path to ebook: ")
        return str(Path(data))

