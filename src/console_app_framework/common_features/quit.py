from src.console_app_framework.feature import Feature


class Quit(Feature):
    HELP = "Quit"

    def run(self, interface, **kwargs):
        exit(0)
