# 23031 A5AYR70100  Power supply Assy /230V
# 24350 QM4-6672-000 резак с направляющей и мотором
from utils import read_exel, write_to_exel


def delete_duplicate_lines(_list):
    counter = 0
    temp_list = _list[:]
    duplicate_list = []
    for i in range(23031, 24350):
        for j in range(17, 23029):
            if _list[i][1] == temp_list[j][1]:
                if temp_list[i][1] is None:
                    pass
                else:
                    _list[i][1] = ''
    for i in range(len(temp_list)):
        duplicate_list.append(temp_list[i][1])
    temp_list.clear()
    for i in range(len(_list)):
        temp_list.append(_list[i][1])
    for i in range(len(temp_list)):
        if duplicate_list[i] != temp_list[i]:
            print(counter)
            counter += 1
    return duplicate_list


parts_list = read_exel()
deleted_list = delete_duplicate_lines(parts_list)
write_to_exel(deleted_list, 'backup/deleted.xlsx')
