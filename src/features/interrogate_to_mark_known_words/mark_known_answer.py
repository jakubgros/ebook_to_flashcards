from src.features.feature import Feature


class MarkKnownAnswer(Feature):
    HELP = "Answer known"

    def run(self, interface, *, word, it, **kwargs):
        word.mark_if_known(True)
        it.next()
