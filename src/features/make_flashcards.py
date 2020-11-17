from src.database import Database
from src.features.chose_book import ChoseBook
from src.features.feature import Feature
from src.translator.translator import Translator


class MakeFlashcards(Feature):
    HELP = "Allows to make a flashcards from unknown words from a book"

    def run(self, interface, book, **kwargs):
        book = ChoseBook().run(interface, **kwargs)

        if not book.are_all_words_processed():
            interface.display_info("The book is not fully processed. Please firstly mark known words. ")
            return

        translator = Translator()

        unknown_words_cnt = len(book.unknown_words)
        for idx, word in enumerate(book.unknown_words):
            word_translations = translator.get_translation(word.stored_word)
            prompt = self.get_translation_choice_prompt(idx, unknown_words_cnt, word_translations)

            def answ_validator(str_val):
                try:
                    int_val = int(str_val)
                    if 0 <= int_val < len(word_translations):
                        return True
                except:
                    pass
                return False

            choice = interface.get_input(prompt, input_validator=answ_validator)
            choice = int(choice) #TODO input_validator could also make the conversion

            chosen_translation = word_translations[choice]
            flashcard = ", ".join(chosen_translation.word) + "=" + ", ".join(chosen_translation.meaning)
            book.flashcards.append(flashcard)

            word.mark_if_known(True)

        db = Database()
        db.store_book(book)

    def get_translation_choice_prompt(self, idx, unknown_words_cnt, word_translations):
        out = f"[curr translation {idx}/{unknown_words_cnt}]" \

        for idx, translation in enumerate(word_translations):
            out += f"\n>> {', '.join(translation.word)}\n"\
                   f"\t[{idx}] {', '.join(translation.meaning)}"

            for example_and_its_translation in translation.examples_and_its_translations:
                out += f"\n\t\t{' '.join(example_and_its_translation)}"

        out += "\nYour choice"
        return out
