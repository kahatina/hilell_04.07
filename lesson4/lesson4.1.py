import copy

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

copy_of_lst = copy.deepcopy(lst)

for n in lst:
    if n == 0:
        copy_of_lst.remove(n)
        copy_of_lst.append(0)

print(copy_of_lst)