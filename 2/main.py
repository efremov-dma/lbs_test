import argparse
import sys
from collections import Counter
from typing import List, Tuple

from input import Input


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
def main(x: List[str], y: List[str]) -> List[int]:
    """
    :param x:
    :param y:
    :return: List[int]
    """
    return [Counter(x)[request] for request in y]


def _read_from_file(fname: str) -> Tuple[List[str], List[str]]:
    """
    Reads an input data from file.
    :param fname: str
    :return: List[str]
    """
    with open(fname) as f:
        lines = f.read().splitlines()

    x_len, x = _parse_data(lines)
    y_len, y = _parse_data(lines[x_len + 1:])

    return x, y


def _parse_data(lines: List[str]) -> Tuple(int, List[str]):
    """
    Returns number of lines and list of lines.
    :param lines:
    :return:
    """
    length = lines[0]
    if not length.isdigit():
        raise ValueError('Invalid list length value.')

    length = int(length)

    return length, lines[1:length + 1]


def _get_user_input() -> Tuple[List[str], List[str]]:
    """
    Gets data from user input.
    :return: Tuple[List[str], List[str]]
    """
    return _get_lines('X'), _get_lines('Y')


def _get_lines(list_name) -> List[str]:
    """
    Gets lines from user input.
    :param list_name:
    :return: List[str]
    """
    lines = []
    length = Input.positive_int('Введите количество элементов {}:'.format(list_name))

    for _ in range(length):
        lines.append(Input.alphastr('Введите строку {}:'.format(list_name)))

    return lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='read input data from file')
    args = parser.parse_args()

    if args.file:
        X, Y = _read_from_file(fname=args.file)
    else:
        X, Y = _get_user_input()

    try:
        main(X, Y)
    except Exception as e:
        sys.exit('Unexpected error: ' + str(e))
