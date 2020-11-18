class Feature:
    HELP = None

    def __init__(self):
        from src.event_handler import EventHandler

        if hasattr(self, 'input_to_feature'):
            self.event_handler = EventHandler(self.input_to_feature)

    #TODO jagros add validation to Feature class that everything that is needed by features is passed to process
    def run(self, interface, **kwargs):
        raise NotImplementedError

    def run_event_loop(self, interface, **kwargs):
        while True:
            feature_str = interface.get_input("Your choice", input_validator=lambda answ: answ in self.input_to_feature)
            ret = self.event_handler.process(interface, feature_str, **kwargs)

            if ret is not None:
                return ret
