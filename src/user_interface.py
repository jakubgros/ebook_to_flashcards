from pathlib import Path

from src.iterator import Iterator


class UserInterface:
    ANSWER_KNOWN = "KNOWN"
    ANSWER_UNKNOWN = "UNKNOWN"
    PREVIOUS = "PREVIOUS"
    NEXT = "NEXT"
    QUIT = "QUIT"
    NEXT_NOT_PROCESSED = "NEXT_NOT_PROCESSED"
    PREVIOUS_NOT_PROCESSED = "PREVIOUS_NOT_PROCESSED"

    input_to_event_mapping = {
        "q": ANSWER_KNOWN,
        "w": ANSWER_UNKNOWN,
        "back": PREVIOUS,
        "fwd": NEXT,
        "quit": QUIT,
        "fwd np": NEXT_NOT_PROCESSED,
        "back np": PREVIOUS_NOT_PROCESSED,
    }

    def get_event(self):
        while True:
            answ = input()

            if answ in self.input_to_event_mapping:
                return self.input_to_event_mapping[answ]

            print("Invalid input, try again")
            continue

    def display_word(self, word, idx, size):
        progress = f"[{idx + 1}/{size}]"

        if not word.is_checked:
            status = "[?]"
        else:
            status = f"{'[y]' if word.is_known else '[n]'}"

        print(f"{progress} {status} {word.word}: ", end="")

    def _display_info(self, information):
        print(information)

    def process(self, book):
        size = len(book.words_list)
        it = Iterator(book.words_list)

        while not book.are_all_words_processed():
            idx, word = it.get()
            self.display_word(word, idx, size)

            event = self.get_event()

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

            elif event == UserInterface.QUIT:
                return

            else:
                raise Exception("Invalid interface answer")

    def get_path_of_ebook_to_process(self):
        data = input("Enter path to ebook: ")
        return str(Path(data))

