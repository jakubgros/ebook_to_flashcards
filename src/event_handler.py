
class EventHandler:
    def __init__(self, event_to_function, input_to_event_mapping, event_types):
        self.event_to_function = event_to_function
        self.input_to_event_mapping = input_to_event_mapping

    def process(self, interface, event, **kwargs):
        feature = self.event_to_function[event]
        return feature.run(interface, **kwargs)

