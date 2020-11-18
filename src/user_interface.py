class Interface:
    def display_info(self, txt):
        print(txt)

    def get_input(self, prompt, *, input_processor):
        while True:
            answ = input(prompt + ": ")

            processor = input_processor(answ)
            if processor.is_valid():
                return processor.get_processed_value()
            else:
                print(">> Invalid input, try again")