def difference(*args: float) -> float:
    lst_numbers = list(args)
    if not lst_numbers:
        result = 0
    else:
        min_number = min(lst_numbers)
        max_number = max(lst_numbers)
        result = round(max_number - min_number, 2)

    return result