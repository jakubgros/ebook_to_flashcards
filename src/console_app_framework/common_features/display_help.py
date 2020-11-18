from src.console_app_framework.feature import Feature


class DisplayHelp(Feature):
    HELP = "Displays info"

    def run(self, interface, *, input_to_feature, **kwargs):
        for command, feature in input_to_feature.items():
            interface.display_info(f"\t{command} = {feature.HELP}")
