from src.console_app_framework.feature import Feature


class GoToPrevious(Feature):
    HELP = "Go back"

    def run(self, interface, *, it, **kwargs):
        success = it.previous()
        if not success:
            interface.display_info("can't go back")