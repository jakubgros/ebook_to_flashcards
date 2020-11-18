class Feature:
    HELP = None

    def __init__(self):
        from src.event_handler import EventHandler

        if hasattr(self, 'input_to_feature'):
            self.event_handler = EventHandler(self.input_to_feature)

    #TODO jagros add validation to Feature class that everything that is needed by features is passed to process
    def run(self, interface, **kwargs):
        raise NotImplementedError

    def run_event_loop(self, interface, display_help, **kwargs):
        while True:
            if display_help:
                self.event_handler.process(interface, "help")

            feature_str = interface.get_input("Your choice", input_processor=self.event_handler.input_processor)
            if display_help and feature_str == "help":  # so as not to display help twice
                continue

            ret = self.event_handler.process(interface, feature_str, **kwargs)

            if ret is not None:
                return ret
