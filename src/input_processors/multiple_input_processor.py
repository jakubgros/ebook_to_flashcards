from src.input_processors.input_processor import InputProcessor


class MultipleInputProcessor(InputProcessor):
    def __init__(self, single_input_processor):
        self.single_input_processor = single_input_processor

    def is_valid(self):
        temp_processed_values = []
        split_values = self._val_to_process.split(',')
        for value in split_values:
            single_input_processor = self.single_input_processor(value)
            if not single_input_processor.is_valid():
                return False
            else:
                temp_processed_values.append(single_input_processor.get_processed_value())

        self._processed_value = temp_processed_values
        return True


