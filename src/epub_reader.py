import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


class EpubReader:
    def __init__(self, ebook_path):
        self.ebook_path = ebook_path

    def get_text(self):
        book = epub.read_epub(self.ebook_path)
        chapters = [item.get_content() for item in book.get_items() if item.get_type() == ebooklib.ITEM_DOCUMENT]
        text_by_chapter = [self._chapter_to_text(ch) for ch in chapters]
        return " ".join(text_by_chapter)

    @staticmethod
    def _chapter_to_text(chap):
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head',
            'input',
            'script',
        ]

        soup = BeautifulSoup(chap, 'html.parser')
        text = soup.find_all(text=True)

        filtered_text = [t for t in text if t.parent.name not in blacklist]
        return " ".join(filtered_text)
