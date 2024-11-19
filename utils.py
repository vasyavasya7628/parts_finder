import re

from openpyxl.workbook import Workbook
from python_calamine import CalamineWorkbook


def find_matches_for_word(word, _list, cur_index):
    for i in range(len(_list)):
        if i == cur_index:
            pass
        else:
            sentence = _list[i][1].split()


def read_exel(filename='test.xlsx', sheet_name='Лист1'):
    workbook = CalamineWorkbook.from_path(f'{filename}')
    return workbook.get_sheet_by_name(f'{sheet_name}').to_python(skip_empty_area=False)


"""
Находит номера деталей, далее в функции find_matches_for_word начинает перебирать список parts_list для поиска совпадений
"""


def write_to_exel(data, filename="output.xlsx"):
    flattened_data = []
    wb = Workbook()
    ws = wb.active

    for index, value in enumerate(data, start=1):
        ws.cell(row=index, column=1, value=value)

    wb.save(f'{filename}')


def find_duplicates(parts):
    parts_copy = parts[:]  # Создаем копию списка
    parts_duplicate = []

    for i in range(len(parts)):
        for j in range(len(parts)):
            if i != j and parts[i] == parts_copy[j]:
                parts_duplicate.append((j, ' '.join(map(str, parts[i]))))  # Храним индекс и значение
                break  # Прерываем цикл, если нашли дубликат

    result = [''] * len(parts)  # Создаем список нужной длины
    for i, value in parts_duplicate:
        result[i] = value  # Заполняем список по индексам
    print(result)
    return result


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
            if (re.match(pattern, sentence[j])
                    or re.match(r'^\d{5,}$', sentence[j])
                    or re.match(r'^\d{4}-\d{4}$', sentence[j])
                    or re.match(r'^[A-Z]+\d{4,5}-[A-Z]?\d{4,5}(/[A-Z]?\d{4,5})?$', sentence[j])):
                counter += 1
                parts_temp_store.append(sentence[j])
            else:
                pass
        if counter == 0:
            part_number_names.append('')
        else:
            part_number_names.append(parts_temp_store)

    return part_number_names


def join_sublist(input_list):
    # Удаляем пустые строки и объединяем элементы каждого подсписка
    return [[' '.join(sublist)] if sublist else [''] for sublist in input_list]
