
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
    try:
        ui.process(book)
    except:
        db.store_book(book)
    else:
        db.store_book(book)

if __name__ == "__main__":
    main()


#TODO jagros add command to switch to next_unprocessed_word
# TODO jagros make file storage function that behaves as a set
#add help that prints all commands
#TODO move the ebook to the directory with data
#change processing mechanism have regard to already processed words from other books