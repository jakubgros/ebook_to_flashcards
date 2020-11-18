from src.features.feature import Feature


class GoToNext(Feature):
    HELP = "Go forward"

    def run(self, interface, *, it, **kwargs):
        success = it.next()
        if not success:
            interface.display_info("can't go forward")