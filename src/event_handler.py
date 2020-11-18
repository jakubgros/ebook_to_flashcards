from src.features.common.display_help import DisplayHelp
from src.features.common.quit import Quit
from src.input_processors.key_exists_in_map_processor import KeyExistsInMapProcessor


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
        self.input_to_feature = input_to_feature.copy()
        self.input_to_feature.update(input_to_common_features)

        self.input_processor = KeyExistsInMapProcessor(self.input_to_feature)

    def process(self, interface, input_choice, **kwargs):
        feature = self.input_to_feature[input_choice]
        kwargs['input_to_feature'] = self.input_to_feature
        return feature.run(interface, **kwargs)


