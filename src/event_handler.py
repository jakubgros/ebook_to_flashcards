from src.features.feature import Feature

class DisplayHelp(Feature):
    HELP = "Displays info"

    def run(self, interface, *, input_to_feature, **kwargs):
        for command, feature in input_to_feature.items():
            interface.display_info(f"\t{command} = {feature.HELP}")

class EventHandler:
    help_command = 'help'

    def __init__(self, input_to_feature):
        if self.help_command in input_to_feature:
            raise Exception(f"the '{self.help_command}' feature name is reserved. ")

        self.input_to_feature = input_to_feature
        self.input_to_feature[self.help_command] = DisplayHelp()

    def process(self, interface, input_choice, **kwargs):
        feature = self.input_to_feature[input_choice]
        kwargs['input_to_feature'] = self.input_to_feature
        return feature.run(interface, **kwargs)

