lst = [1, 2, 3, [1, 2, 3]]

for i, x in enumerate(lst):
    if isinstance(x, list):
        lst[i] = ' '.join(map(str, x))
print(lst)
# 1, 2, 3, '1 2 3'
