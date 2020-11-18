from src.console_app_framework.input_processors.input_processor import InputProcessor


class KeyExistsInMapProcessor(InputProcessor):
    def __init__(self, a_map):
        self.a_map = a_map

    def is_valid(self):
        if self._val_to_process in self.a_map:
            self._processed_value = self._val_to_process
            return True
        else:
            return False
