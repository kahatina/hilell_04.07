def multiplication_nums(number):
    list_numbers = list(number)
    result = 1

    for num in range(0, len(list_numbers)):
        result *= int(list_numbers[num])
    return result

number = input("Введіть число: ")
new_result = multiplication_nums(number)

while new_result > 9:
    new_result = multiplication_nums(str(new_result))

print(new_result)