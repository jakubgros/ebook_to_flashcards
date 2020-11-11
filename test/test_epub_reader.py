import unittest

from src.env_utils.base_dir import base_dir
from src.epub_reader import EpubReader


class EpubReaderTest(unittest.TestCase):
    def test_reading_text(self):
        reader = EpubReader(f"{base_dir}/test/data/book.epub")
        text = reader.get_text()
        self.assertTrue(len(text) > 0)

if __name__ == '__main__':
    unittest.main()
