with open('task2.txt') as f:
    for i, elem in enumerate(f.readlines(), 1):
        print(f'{i} - кол-во слов: {len(elem.split())}')
