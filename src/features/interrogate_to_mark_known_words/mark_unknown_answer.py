from src.features.feature import Feature


class MarkUnknownAnswer(Feature):
    HELP = "Answer unknown"

    def run(self, interface, *, word, it, **kwargs):
        word.mark_if_known(False)
        it.next()
