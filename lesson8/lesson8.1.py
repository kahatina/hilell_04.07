def add_one(some_list: list) -> list:
    string_numbers = [str(item) for item in some_list]
    full_string_numbers = "".join(string_numbers)
    number = int(full_string_numbers)
    new_number = number + 1
    new_str_some_list = list(str(new_number))
    final_result = [int(m) for m in new_str_some_list]

    return final_result