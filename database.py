from pathlib import Path



class Database:
    data_path = "data/"
    all_words_dir = data_path + "all_words.txt"

    def _create_subdir(self, subdir_name):
        path = Path(self.data_path + "/" + subdir_name)
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    def _extend_known_words(self, words_list):
        with open(self.all_words_dir, 'w+') as out_file:
            for word in words_list:
                print(word.word, file=out_file)

    def _store_to_file(self, file_path, data):
        with open(file_path + "\\book.json", 'w+') as out_file:
            print(data, file=out_file)

    def _store_unknown_words(self, save_dir, words):
        with open(save_dir + "\\unkown_words.txt", 'w+') as out_file:
            for word in words:
                print(word.word, file=out_file)

    def store_book(self, book):
        save_dir = self._create_subdir(book.name)
        data = book.serialize()
        self._store_to_file(save_dir, data)
        self._store_unknown_words(save_dir, book.unknown_words)

        self._extend_known_words(book.known_words)