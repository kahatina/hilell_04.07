lst = []
l = len(lst)

if not lst:
    new_lst = ([], [])
    print(new_lst)

elif l % 2 == 0:
    x = l // 2
    list1 = lst[:x]
    list2 = lst[x:]
    new_lst = [list1, list2]
    print(new_lst)

elif l % 2 != 0:
    x = (l + 1) // 2
    list1 = lst[:x]
    list2 = lst[x:]
    new_lst = [list1, list2]
    print(new_lst)



