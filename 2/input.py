import os


class Input:
    @staticmethod
    def positive_int(prompt: str = '') -> int:
        while True:
            value = input(prompt + os.linesep).strip()

            if not value.isdigit():
                print('Input should be an integer.')
                continue

            int_value = int(value)

            if int_value <= 0:
                print('Input should be greater than zero.')
                continue

            return int_value

    @staticmethod
    def alphastr(prompt: str = '') -> str:
        while True:
            value = input(prompt + os.linesep).strip()

            if len(value) == 0:
                print('Input could not be an empty string.')
                continue

            if not value.isalpha():
                print('Input should contain only alphabetic characters.')
                continue

            return value
