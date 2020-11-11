import unittest

from src.book import Book
from src.env_utils.base_dir import base_dir


class BookTest(unittest.TestCase):

    def test_creation_from_file(self):
        data_dir = f"{base_dir}\\test\\data\\"
        file_name = "book.epub"

        book = Book.from_path(data_dir + file_name)

        self.assertEqual(len(book.known_words), 0)
        self.assertEqual(len(book.unknown_words), 0)
        self.assertEqual(len(book.meaning), 0)

        self.assertEqual(len(book.words), 6349)

        self.assertEqual(book.name, file_name)
        self.assertEqual(book.path, data_dir+file_name)

    def test_known_and_unknown_words_getters(self):
        data_dir = f"{base_dir}\\test\\data\\"
        file_name = "book.epub"

        book = Book.from_path(data_dir + file_name)

        self.assertEqual(len(book.known_words), 0)
        self.assertEqual(len(book.unknown_words), 0)

        known_words_to_mark = {"the", "it", "on"}
        for word in book.words:
            if word.word in known_words_to_mark:
                word.mark(True)

        self.assertEqual({w.word for w in book.known_words}, known_words_to_mark)

        unknown_words_to_mark = {"she", "he"}
        for word in book.words:
            if word.word in unknown_words_to_mark:
                word.mark(False)

        self.assertEqual({w.word for w in book.unknown_words}, unknown_words_to_mark)

    def test_are_all_words_processed(self):
        data_dir = f"{base_dir}\\test\\data\\"
        file_name = "book.epub"

        book = Book.from_path(data_dir + file_name)

        self.assertFalse(book.are_all_words_processed())

        for word in book.words:
            word.mark(True)

        self.assertTrue(book.are_all_words_processed())


if __name__ == '__main__':
    unittest.main()
