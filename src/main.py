from src.database import Database
from src.interface.features.show_main_menu_feature import ShowMainMenuFeature
from src.interface.user_interface import Interface


def main():

    interface = Interface()
    ShowMainMenuFeature.run(interface)
    #TODO implement stack for handling feature calls. Quit => stack.popAll

    """"
        db = Database()

    data = input("Enter path to ebook: ")
    book_path = str(Path(data))
    book = Book.from_path(book_path)

    if db.has_book(book.name):
        book = db.restore_book(book.name)

    known_words = db.get_known_words()
    for word in book.words:
        if word.stored_word in known_words:
            word.mark_if_known(True)

    try:
        if not book.are_all_words_processed():
            feat = InterrogateToMarkKnownWordsFeature()
            feat.run(interface, book)
    finally:
        db.store_book(book)

    """



if __name__ == "__main__":
    main()
