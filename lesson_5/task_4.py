change = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('task4a.txt') as f1:
    with open('task4b.txt', 'w') as f2:
        for elem in f1.readlines():
            tmp_list = elem.strip().split(' - ')
            tmp_list[0] = change[tmp_list[0]]
            print(' - '.join(tmp_list), file=f2)
