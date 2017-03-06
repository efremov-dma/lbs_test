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
    def alphanumeric_str(prompt: str = '') -> str:
        while True:
            value = input(prompt + os.linesep).strip()

            if len(value) == 0:
                print('Input could not be an empty string.')
                continue

            if not all(char.isalnum() or char.isspace() for char in value):
                print('Input should contain only alphabetic characters.')
                continue

            return value
