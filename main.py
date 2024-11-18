"""
    В номере детали есть цифра, буква (не всегда), или буква, цифра, спецсимвол. Минимальная длина 8 символов
    Проверить дубли начиная со строки 23031 по 24350
"""

# print(partnumber_list[23031])
# print(partnumber_list[24350])
# print(parts_list)

from utils import find_partnumber, write_to_exel, find_duplicates, read_exel

list_ = read_exel('test.xlsx', 'Лист1')
partnumber_list = find_partnumber(list_)
duplicate_list = find_duplicates(partnumber_list)
write_to_exel(duplicate_list)
