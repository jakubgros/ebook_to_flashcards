
from src.book import Book
from src.database import Database
from src.user_interface import UserInterface

def main():
    db = Database()
    ui = UserInterface()

    book_path = ui.get_path_of_ebook_to_process()
    book = Book.from_path(book_path)

    if db.has_book(book):
        book = db.restore_book(book)


    known_words = db.get_known_words()
    book.mark_known_words(known_words)

    try:
        ui.process(book)
    finally:
        db.store_book(book)

if __name__ == "__main__":
    main()


#TODO jagros add command to switch to next_unprocessed_word
#add help that prints all commands
#TODO move the ebook to the directory with data
