import re


class Preprocessor:
    @staticmethod
    def process(txt):
        regex = re.compile('[^a-zA-Z]')
        txt = regex.sub(' ', txt).lower().split()
        return [word for word in txt if len(word) != 1]
