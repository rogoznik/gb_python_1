import json

res_list = []
firm_dict = {}
ave_profit_dict = {}
count_firm = 0
sum_firm = 0
with open('task7a.txt') as f1:
    for elem in f1.readlines():
        elem_list = elem.split()
        key_dict = elem_list[0]
        c = int(elem_list[2]) - int(elem_list[3])
        if c > 0:
            count_firm += 1
            sum_firm += c
        firm_dict.update({key_dict: c})

ave_profit_dict.update({'average_profit': sum_firm / count_firm})
res_list.append(firm_dict)
res_list.append(ave_profit_dict)

print(res_list)

with open('task7b.json', 'w') as f2:
    f2.write(json.dumps(res_list))
