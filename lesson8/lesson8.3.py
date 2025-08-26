def find_unique_value(some_list: list) -> float:
    for el in some_list:
        if some_list.count(el) == 1:
            return el