import argparse
import sys
from collections import namedtuple
from typing import List

from errors import LineFormatError
from input import Input

ParsedLine = namedtuple('ParsedLine', ['fname', 'lname', 'sex', 'age'])

SEX_MAP = {
    'female': 'Ж',
    'male': 'М',
}


def parse_data(func):
    """
    Decorator to parse data lines.
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        for index, line in enumerate(data):
            data[index] = _parse_line(line)

        return data

    return wrapper


def print_output(func):
    """
    Decorator to print an output of a given function to shell.
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):

        output = func(*args, **kwargs)

        try:
            for item in output:
                print(item)

        except TypeError:
            print(output)

    return wrapper


@print_output
def main(data: list):
    """
    :param data: list
    """
    data.sort(key=lambda line: line.age)

    for index, line in enumerate(data):
        data[index] = _format_output_line(line)

    return data


@parse_data
def _read_from_file(fname: str) -> List[str]:
    """
    Reads an input data from file and returns a list of lines.
    :param fname: str
    :return: List[str]
    """
    with open(fname) as f:
        lines = f.read().splitlines()

    limit = lines[0]
    if not limit.isdigit():
        raise ValueError('Invalid limit value.')

    return lines[1:int(limit) + 1]


@parse_data
def _get_user_input() -> List[str]:
    """
    Reads user input and returns a list of lines.
    :return: List[str]
    """
    data = []

    limit = Input.positive_int('Введите количество строк:')

    for _ in range(limit):
        data.append(Input.alphanumeric_str('Введите строку в формате "<Имя> <Фамилия> <Пол М/Ж> <Возраст>":'))

    return data


def _get_honorific_title(sex: str) -> str:
    """
    Returns the corresponding honorific title for a given sex value.
    :param sex: str
    :return: str
    """
    if sex == SEX_MAP['female']:
        return 'Г-жа'

    if sex == SEX_MAP['male']:
        return 'Г-н'

    raise ValueError('Unexpected sex value.')


def _parse_line(line: str) -> ParsedLine:
    """
    Parses a string in format "<First Name> <Last Name> <Sex М/Ж> <Age>"
    and returns a parsed line object or raises an exception if string
    has invalid format.
    :param line: str
    :return: ParsedLine
    """
    values = line.split()

    if len(values) != 4:
        raise LineFormatError('Invalid number of values in line.')

    sex = values[2]
    if sex not in SEX_MAP.values():
        raise LineFormatError('Invalid sex value.')

    age = values[3]
    if not age.isdigit():
        raise LineFormatError('Invalid age value.')

    values[3] = int(age)

    return ParsedLine._make(values)


def _format_output_line(line: ParsedLine) -> str:
    """
    Converts a given parsed line to an appropriate output
    format "<Honorific Title> <First Name> <Last Name>"
    :rtype: str
    """
    return '{title} {fname} {lname}'.format(
        title=_get_honorific_title(line.sex),
        fname=line.fname,
        lname=line.lname
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='read input data from file')
    args = parser.parse_args()

    if args.file:
        data = _read_from_file(fname=args.file)
    else:
        data = _get_user_input()

    try:
        main(data)
    except LineFormatError as e:
        sys.exit('Line format error: ' + str(e))
    except Exception as e:
        sys.exit('Unexpected error: ' + str(e))
