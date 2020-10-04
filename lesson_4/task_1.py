import argparse
from sys import argv


def create_parser():
    parser = argparse.ArgumentParser(description='Расчет заработной платы сотрудника')
    parser.add_argument('production', type=float, nargs='?', help='Выработка в часах')
    parser.add_argument('rate', type=float, nargs='?', help='Ставка в часах')
    parser.add_argument('prize', type=float, nargs='?', help='Премия')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(argv[1:])

    if namespace.production is not None and namespace.rate is not None and namespace.prize is not None:
        res = (namespace.production * namespace.rate) + namespace.prize
        print(f'Зарплата: {res}')
    else:
        print('Ошибка: укзаны не все параметры')
