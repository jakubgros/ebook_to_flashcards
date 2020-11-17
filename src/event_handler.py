
class EventHandler:
    def __init__(self, event_to_function):
        self.event_to_function = event_to_function

    def process(self, interface, event, **kwargs):
        feature = self.event_to_function[event]
        return feature.run(interface, **kwargs)

