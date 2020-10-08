res_dict = {}
with open('task6.txt') as f:
    for elem in f.readlines():
        tmp_list = elem.split()
        key_dict = ''
        sum_key = 0
        for i in range(len(tmp_list)):
            if i == 0:
                key_dict = tmp_list[i][:len(tmp_list[0]) - 1]
                continue
            if tmp_list[i] == '-':
                continue
            sum_key += int(tmp_list[i][:tmp_list[i].find('(')])
        res_dict.update({key_dict: sum_key})

print(res_dict)
