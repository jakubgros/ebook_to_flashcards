from book import Book
from database import Database
from user_interface import UserInterface

if __name__ == "__main__":
    book = Book("book.epub")

    ui = UserInterface()

    ui.process(book)

    db = Database()
    db.store_book(book)



#TODO jagros crash recover
#TODO jagros make it possible to close program in the middle of processing and then restart it and continue
#TODO jagros add command to switch to next_unprocessed_word
# TODO jagros make file storage function that behaves as a set
#add help that prints all commands
#TODO move the ebook to the directory with data