from src.features.feature import Feature


class DisplayHelp(Feature):

    def __init__(self):
        pass

    def run(self, interface, *, input_to_feature, **kwargs):
        for command, (_, description) in input_to_feature.items():
            interface.display_info(f"\t{command} = {description}")