lst = []
if lst == []:
    print(lst)
else:
    num = lst.pop(-1)
    lst.insert(0, num)
    print(lst)