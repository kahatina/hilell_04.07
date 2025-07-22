lst = [1, 3, 5]

if lst == []:
    result = 0
else:
    numbers = lst[::2]
    suma = sum(numbers)
    result = suma * lst[-1]

print(result)