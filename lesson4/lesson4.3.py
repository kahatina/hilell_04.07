import random

lst = []
lenght_of_lst = random.randint(3, 10)

while len(lst) != lenght_of_lst:
    num = random.randint(1, 10)
    lst.append(num)


lst2 = [lst[0], lst[2], lst[-2]]
