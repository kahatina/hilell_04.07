def add_one(some_list):
    string_numbers = [str(item) for item in some_list]
    full_string_numbers = "".join(string_numbers)
    number = int(full_string_numbers)
    new_number = number + 1
    new_str_some_list = list(str(new_number))
    final_result = [int(m) for m in new_str_some_list]

    return final_result




assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
