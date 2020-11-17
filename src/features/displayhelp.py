from src.features.feature import Feature


class DisplayHelp(Feature):

    def __init__(self):
        pass

    def run(self, interface, *, input_to_event_mapping, **kwargs):
        for command, description in input_to_event_mapping.items():
            interface.display_info(f"\t{command} = {description}")