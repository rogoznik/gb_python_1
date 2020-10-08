import random

with open('task5.txt', 'w+') as f:
    str_for_file = ''
    for i in range(10):
        str_for_file += str(random.randint(1, 100)) + ' '

    f.write(str_for_file.strip())
    f.seek(0)

    print(sum(list(map(int, f.read().split()))))

