from src.features.feature import Feature


class DisplayHelp(Feature):

    def __init__(self):
        pass

    def run(self, interface, **kwargs):
        for command, (_, description) in kwargs['input_to_event_mapping'].items():
            interface.display_info(f"\t{command} = {description}")