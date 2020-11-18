from src.input_processors.input_processor import InputProcessor


class IntInRangeInputProcessor(InputProcessor):
    def __init__(self, *, valid_range):
        self.greater_or_equal_than, self.lower_than = valid_range

    def is_valid(self):
        try:
            self._processed_value = int(self._val_to_process)
            if self.greater_or_equal_than <= self._processed_value < self.lower_than:
                return True
        except:
            pass
        return False