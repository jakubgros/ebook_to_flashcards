from src.features.common.display_help import DisplayHelp
from src.features.common.quit import Quit


class EventHandler:
    def _validate_inputs_mapping(self, received_input_to_feature_mapping, reserved_commands):
        duplicated_commands = [command for command in reserved_commands if command in received_input_to_feature_mapping]
        if duplicated_commands:
            raise Exception(f"The following feature names are reserved: {', '.join(duplicated_commands)}. ")

    def __init__(self, input_to_feature):
        input_to_common_features = {
            'help': DisplayHelp(),
            'quit': Quit(),
        }

        self._validate_inputs_mapping(input_to_feature, input_to_common_features.keys())
        self.input_to_feature = input_to_feature
        self.input_to_feature.update(input_to_common_features)

    def process(self, interface, input_choice, **kwargs):
        feature = self.input_to_feature[input_choice]
        kwargs['input_to_feature'] = self.input_to_feature
        return feature.run(interface, **kwargs)

