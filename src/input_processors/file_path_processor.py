import os
from src.input_processors.input_processor import InputProcessor


class FilePathProcessor(InputProcessor):
    def is_valid(self):
        if os.path.isfile(self._val_to_process):
            self._processed_value = self._val_to_process
            return True
        else:
            return False
