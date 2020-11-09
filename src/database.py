import json
import os
from pathlib import Path

from src.book import Book
from src.env_utils.base_dir import base_dir
from src.serialization.serializer_manager import SerializerManager


class Database:
    data_path = f"{base_dir}/data/"
    all_words_dir = data_path + "all_words.txt"

    def has_book(self, book):
        book_uri = self.get_book_uri(book.name) + "//book.json"
        return os.path.isfile(book_uri)

    def restore_book(self, book):
        book_uri = self.get_book_uri(book.name)
        book_uri += "//book.json"
        with open(book_uri) as book_in:
            json_data = json.loads(book_in.read())

        return SerializerManager.deserialize(json_data)

    def _create_subdir(self, full_dir):
        path = Path(full_dir)
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    def _extend_known_words(self, words_list):
        with open(self.all_words_dir, 'w+') as out_file:
            for word in words_list:
                print(word.word, file=out_file)

    def _store_to_file(self, file_path, data):
        with open(file_path + "\\book.json", 'w+') as out_file:
            print(data, file=out_file)

    def _store_unknown_words(self, save_dir, words):
        with open(save_dir + "\\unkown_words.txt", 'w+') as out_file:
            for word in words:
                print(word.word, file=out_file)

    def get_book_uri(self, book_name):
        return self.data_path + "/" + book_name

    def store_book(self, book):
        book_uri = self.get_book_uri(book.name)
        save_dir = self._create_subdir(book_uri)
        data = json.dumps(SerializerManager.serialize(book), indent=4, sort_keys=True)
        self._store_to_file(save_dir, data)
        self._store_unknown_words(save_dir, book.unknown_words)

        self._extend_known_words(book.known_words)