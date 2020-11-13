class EventHandler:
    def __init__(self, event_type_to_function_and_description):
        self.event_type_to_function_and_description = event_type_to_function_and_description

    def process(self, event, data):
        feature = self.event_type_to_function_and_description[event.type]
        feature.function(event, data)