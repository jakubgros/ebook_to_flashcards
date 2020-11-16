class Interface:
    def display_info(self, txt):
        print(txt)

    def get_input(self, prompt, *, input_validator=None):
        while True:
            answ = input(prompt + ": ")
            if input_validator is None or input_validator(answ):
                return answ
            else:
                print(">> Invalid input, try again")


















    ''''
    
    
    
    
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
            event = self._get_event(event_prompt, input_to_event_mapping)

            if event == EventTypes.HELP:
                for command, (_, description) in self.input_to_event_mapping.items():
                    print(f"\t{command} = {description}")

            elif event == UserInterface.QUIT:
                return

            else:
                raise Exception("Invalid interface answer")


    
    '''