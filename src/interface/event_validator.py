class EventTranslator:
    def __init__(self, mapping):
        self.mapping = mapping

    def is_valid(self, event_str):
        return event_str in self.mapping

    def translate(self, event_str):
        return self.mapping[event_str][0]
