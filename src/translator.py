import dikicli
from dikicli.core import translate

from src.env_utils.base_dir import base_dir


class TranslationUnit:
    def __init__(self, words, meanings, examples_and_its_translations):
        self.words = words
        self.meanings = meanings
        self.examples_and_its_translations = examples_and_its_translations


class Translator:
    def __init__(self):
        self.config = {'data dir': f"{base_dir}/temp/dikicli_cache"}

    def get_translation(self, word):
        try:
            unprocessed_translation = translate(word, self.config)
        except dikicli.core.WordNotFound:
            unprocessed_translation = []

        my_translations = []
        for word, parts_of_speech in unprocessed_translation:
            for _, meanings in parts_of_speech:
                for meaning in meanings:
                    my_translations.append(TranslationUnit(word, meaning.meaning, meaning.examples))

        return my_translations
