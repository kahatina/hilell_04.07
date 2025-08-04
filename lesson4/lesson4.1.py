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