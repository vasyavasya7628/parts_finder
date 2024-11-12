def find_matches_for_word(word, _list, cur_index):
    for i in range(len(_list)):
        if i == cur_index:
            pass
        else:
            sentence = _list[i][1].split()


"""
Находит номера деталей, далее в функции find_matches_for_word начинает перебирать список parts_list для поиска совпадений
"""
import re


def write_to_exel(dublicate_list):
    pass


def find_duplicates(parts):
    parts_copy = parts
    parts_duplicate = []
    mem_index = []
    for i in range(23031,24350):
        for j in range(17, 24350):
            if i == j:
                break
            elif parts_copy[i] == parts[j]:
               mem_index.append(i)

    for i in range(len(parts)):
        found = False
        for j in range(len(mem_index)):
            if i == mem_index[j]:
                found = True
                parts_duplicate.append(parts[i])
        if not found:
            parts_duplicate.append('')
    return parts_duplicate
"""
Находит номера деталей, далее в функции find_matches_for_word начинает перебирать список parts_list для поиска совпадений
"""


def find_partnumber(parts_list=None,
                    pattern='^(?!.*\/)(?=.*\d)(?=.*[a-zA-Z])(?!.*,)(?!.*\()(?!.*\))(?!.*Phaser)(?!.*TASKalfa)(?!.*Taskalfa)[a-zA-Z\d\W+-]{6,}$'):
    part_number_names = []
    for i in range(len(parts_list)):
        sentence = parts_list[i][1].split()
        counter = 0
        parts_temp_store = []
        for j in range(len(sentence)):
            if re.match(pattern, sentence[j]):
                counter += 1
                parts_temp_store.append(sentence[j])
            else:
                pass
        if counter == 0:
            part_number_names.append('')
        else:
            part_number_names.append(parts_temp_store)

    return part_number_names
