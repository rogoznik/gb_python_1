with open('task3.txt') as f:
    staff_list = [elem.split()[0] for elem in f.readlines() if int(elem.split()[1]) < 20000]
    summ_salary = 0
    count = 1
    f.seek(0)
    for elem in f.readlines():
        count += 1
        summ_salary += int(elem.split()[1])

print(staff_list)
print(summ_salary / count)
