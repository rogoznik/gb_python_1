original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def find_in_list(target_list, elem):
    indices = [i for i, x in enumerate(target_list) if x == elem]
    if len(indices) == 1:
        return False
    else:
        return True


res_list = [elem for elem in original_list if not find_in_list(original_list, elem)]

print(res_list)
