
class EventHandler:
    def __init__(self, input_to_feature):
        self.input_to_feature = input_to_feature

    def process(self, interface, input_choice, **kwargs):
        feature = self.input_to_feature[input_choice]
        return feature.run(interface, **kwargs)

