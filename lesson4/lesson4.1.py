lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for n in lst:
    if n == 0:
        lst.remove(n)
        lst.append(0)

print(lst)