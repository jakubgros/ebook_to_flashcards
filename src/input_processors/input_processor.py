class InputProcessor:
    def __call__(self, val_to_process):
        self._val_to_process = val_to_process
        self._processed_value = None
        return self

    def is_valid(self):
        raise NotImplementedError

    def get_processed_value(self):
        if self._processed_value is not None:
            return self._processed_value
        else:
            if self.is_valid():
                return self._processed_value
            else:
                raise ValueError(f"The validated value is invalid: {self._val_to_process}. ")


