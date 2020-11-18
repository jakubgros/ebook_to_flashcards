from src.event_handler import EventHandler


class Feature:
    HELP = None

    def __init__(self):
        if hasattr(self, 'input_to_feature'):
            self.event_handler = EventHandler(self.input_to_feature)

    def run(self, interface, **kwargs):
        raise NotImplementedError



