from itertools import cycle


some_list = [2, 5, 7, 9]
some_cycle_list = cycle(some_list)
counter = 0

for i in some_cycle_list:
    counter += 1
    print(i)
    if counter // len(some_list) == 3:
        break
