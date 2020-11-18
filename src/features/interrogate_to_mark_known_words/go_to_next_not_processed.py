from src.features.feature import Feature


class GoToNextNotProcessed(Feature):
    HELP = "Go forward to next unprocessed word"

    def run(self, interface, *, it, **kwargs):
        success = it.next(lambda w: not w.is_checked)
        if not success:
            interface.display_info("Everything from current point till the end has been processed. Can't jump forward to next unprocessed word. ")