import json
import os
import shutil
from pathlib import Path

from src.env_utils.base_dir import base_dir
from src.serialization.serializer_manager import SerializerManager


class Database:
    data_path = f"{base_dir}/data/"
    known_words_dir = data_path + "known_words.txt"

    def has_book(self, book):
        book_uri = self.get_book_uri(book.name) + "//book.json"
        return os.path.isfile(book_uri)

    def restore_book(self, book):
        book_uri = self.get_book_uri(book.name)
        book_uri += "//book.json"
        with open(book_uri) as book_in:
            json_data = json.loads(book_in.read())

        return SerializerManager.deserialize(json_data)

    def _create_subdir_if_not_exists(self, full_dir):
        path = Path(full_dir)
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    def _extend_known_words(self, words_list):
        out_set = set()

        if os.path.exists(self.known_words_dir):
            with open(self.known_words_dir) as in_file:
                for word in in_file.readlines():
                    out_set.add(word)

        out_set.update([word.word for word in words_list])

        with open(self.known_words_dir, 'w') as out_file:
            for word in out_set:
                print(word, file=out_file)

    def _store_unknown_words(self, save_dir, words):
        with open(save_dir + "\\unkown_words.txt", 'w+') as out_file:
            for word in words:
                print(word.word, file=out_file)

    def get_book_uri(self, book_name):
        return self.data_path + "/" + book_name

    def store_book(self, book):
        book_uri = self.get_book_uri(book.name)
        save_dir = self._create_subdir_if_not_exists(book_uri)

        shutil.copy2(book.path, save_dir)

        data = json.dumps(SerializerManager.serialize(book), indent=4, sort_keys=True)

        with open(save_dir + "\\book.json", 'w+') as out_file:
            print(data, file=out_file)

        self._store_unknown_words(save_dir, book.unknown_words)

        self._extend_known_words(book.known_words)

    def get_known_words(self):
        known_words = set()

        if os.path.exists(self.known_words_dir):
            with open(self.known_words_dir) as in_file:
                for word in in_file.readlines():
                    known_words.add(word)

        return known_words