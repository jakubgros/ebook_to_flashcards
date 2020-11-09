
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


class Preprocessor:
    @staticmethod
    def process(txt):
        import re

        regex = re.compile('[^a-zA-Z]')
        txt = regex.sub(' ', txt)
        txt = txt.lower()

        return [word for word in txt.split() if len(word) != 1]

class EbookReader:
    pass

class EpubReader(EbookReader):

    def __init__(self, ebook_path):
        self.ebook_path = ebook_path

    def get_text(self):
        thtml_by_chapter = self.epub2thtml(self.ebook_path)
        text_by_chapter = self.thtml2ttext(thtml_by_chapter)
        return " ".join(text_by_chapter)


    def epub2thtml(self, epub_path):
        book = epub.read_epub(epub_path)
        chapters = []
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                chapters.append(item.get_content())
        return chapters


    def chap2text(self, chap):
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head',
            'input',
            'script',
            # there may be more elements you don't want, such as "style", etc.
        ]

        output = ''
        soup = BeautifulSoup(chap, 'html.parser')
        text = soup.find_all(text=True)
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)
        return output


    def thtml2ttext(self, thtml):
        Output = []
        for html in thtml:
            text = self.chap2text(html)
            Output.append(text)
        return Output





