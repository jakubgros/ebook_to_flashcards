from src.book import Book
from src.database import Database
from src.env_utils.base_dir import base_dir
from src.user_interface import UserInterface


def main():
    db = Database()
    ui = UserInterface()

    book_path = ui.get_path_of_ebook_to_process()
    book = Book.from_path(book_path)

    if db.has_book(book):
        book = db.restore_book(book)

    known_words = db.get_known_words()
    for word in book.words:
        if word.stored_word in known_words:
            word.mark_if_known(True)

    try:
        if not book.are_all_words_processed():
            ui.interrogate_to_mark_known_words(book)

        #ui.make_flashcards(book)
    finally:
        pass

    db.store_book(book)


if __name__ == "__main__":
    main()
