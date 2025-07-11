# Приклади:
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

lst = []
if lst == []:
    print(lst)
else:
    num = lst.pop(-1)
    lst.insert(0, num)
    print(lst)