"""
    В номере детали есть цифра, буква (не всегда), или буква, цифра, спецсимвол. Минимальная длина 8 символов
    Проверить дубли начиная со строки 23031 по 24350
"""
# import pandas
#
# parts_list = pandas.read_excel(io='test.xlsx',
#                                sheet_name='Лист1',
#                                engine='openpyxl',
#                                usecols='B',
#                                header=16,
#                                nrows=300)
# list_[23031][1]
# print(parts_list)

from python_calamine import CalamineWorkbook

from utils import find_partnumber, write_to_exel, find_duplicates

workbook = CalamineWorkbook.from_path('test.xlsx')
print(workbook.sheet_names)
list_ = workbook.get_sheet_by_name('Лист1').to_python(skip_empty_area=False)

partnumber_list = find_partnumber(list_)
print(type(partnumber_list))
#write_to_exel(partnumber_list)
# duplicates = find_duplicates(partnumber_list)
# print(partnumber_list[23031])
# print(partnumber_list[24350])
# print(len(duplicates))
duplicate_list = find_duplicates(partnumber_list)
write_to_exel(duplicate_list)
