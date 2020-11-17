class Interface:
    def display_info(self, txt):
        print(txt)

    def get_input(self, prompt, *, input_validator=None):
        while True:
            answ = input(prompt + ": ")
            if input_validator is None or input_validator(answ):
                return answ
            else:
                print(">> Invalid input, try again")