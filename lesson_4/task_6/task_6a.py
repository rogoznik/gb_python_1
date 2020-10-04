import argparse
from itertools import count
from sys import argv


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', type=int, nargs='?', help='Целое число')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(argv[1:])

    if namespace.num is not None:
        for i in count(start=namespace.num):
            print(i)
            if i == 30:
                break
    else:
        print('Ошибка: не указали число')
