from src.interface.features.feature import Feature


class display_help(Feature):
    @staticmethod
    def run(interface, **kwargs):
        for command, (_, description) in kwargs['input_to_event_mapping'].items():
            interface.display_info(f"\t{command} = {description}")