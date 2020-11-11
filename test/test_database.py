import shutil
import unittest

from src.book import Book
from src.database import Database
from src.env_utils.base_dir import base_dir
from test.utils import ContainerComparator


class TestDatabase(unittest.TestCase):
    db_handle = f"{base_dir}/temp/testing/"

    def tearDown(self):
        shutil.rmtree(self.db_handle, ignore_errors=True)

    def setUp(self):
        shutil.rmtree(self.db_handle, ignore_errors=True)

    def test_storing_and_restoring_book(self):
        database = Database(self.db_handle)

        book = Book.from_path(f"{base_dir}/test/data/book.epub")
        # small data manipulation to make sure that it was retained when saving to db
        for word in book.words:
            word.mark_if_known(True)

        database.store_book(book)

        restored_book = database.restore_book(book.name)

        words_list_comparator = ContainerComparator(elem_equality_comparator=self._are_words_equal, sort_key=lambda w: w.stored_word)

        self.assertEqual(book.are_all_words_processed(), restored_book.are_all_words_processed())
        self.assertTrue(words_list_comparator(book.known_words, restored_book.known_words))
        self.assertTrue(words_list_comparator(book.unknown_words, restored_book.unknown_words))
        self.assertEqual(book.name, restored_book.name)
        self.assertTrue(words_list_comparator(book.words, restored_book.words))
        self.assertEqual(book.meaning, restored_book.meaning)

    def test_has_book(self):
        database = Database(self.db_handle)
        book_dir = f"{base_dir}/test/data/book.epub"
        book = Book.from_path(book_dir)
        database.store_book(book)
        self.assertTrue(database.has_book(book.name))

    def test_get_known_words(self):
        words_list_comparator = ContainerComparator(elem_equality_comparator=lambda lhs, rhs: lhs == rhs, sort_key=lambda w: w)

        database = Database(self.db_handle)

        self.assertEqual(len(database.get_known_words()), 0)

        book1 = Book.from_path(f"{base_dir}/test/data/book.epub")
        for word in book1.words:
            word.mark_if_known(True)

        book2 = Book.from_path(f"{base_dir}/test/data/book2.epub")
        for word in book2.words:
            word.mark_if_known(True)

        database.store_book(book1)
        database.store_book(book2)

        book1_raw_known_words = set(w.stored_word for w in book1.known_words)
        book2_raw_known_words = set(w.stored_word for w in book2.known_words)
        both_books_words = book1_raw_known_words.union(book2_raw_known_words)

        self.assertTrue(words_list_comparator(database.get_known_words(), both_books_words))

    def _are_words_equal(self, lhs, rhs):
        return lhs.stored_word == rhs.stored_word \
               and lhs.occurrences == rhs.occurrences \
               and lhs.is_known == rhs.is_known \
               and lhs.is_checked == rhs.is_checked \
               and lhs.translations == rhs.translations


if __name__ == '__main__':
    unittest.main()
