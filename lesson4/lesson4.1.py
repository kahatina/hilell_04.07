# Приклад
# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

lst = [1, 0, 13, 0, 0, 0, 5]
lst2 = lst.copy()
i = len(lst2)

while 0 in lst:
        lst.remove(0)
        continue

while len(lst) != len(lst2):
    lst.append(0)
    continue
print(lst)