from src.console_app_framework.feature import Feature


class GoToPreviousNotProcessed(Feature):
    HELP = "Go back to previous unprocessed word"

    def run(self, interface, *, it, **kwargs):
        success = it.previous(lambda w: not w.is_checked)
        if not success:
            interface.display_info("Everything from current point till the beggining has been processed. Can't jump backward to prevuous unprocessed word. ")