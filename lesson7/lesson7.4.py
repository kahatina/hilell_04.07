def common_elements():
    first_list = [num1 for num1 in range(101) if num1 % 3 == 0]
    second_list = [num2 for num2 in range(101) if num2 % 5 == 0]

    set1 = set(first_list)
    set2 = set(second_list)

    multiples = set1.intersection(set2)
    return multiples

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}