def is_even(number: int) -> bool:

    verification_numbers = [0, 2, 4, 6, 8]

    line_number = list(str(number))
    last_line_number = int(line_number[-1])

    for n in verification_numbers:
        if n == last_line_number:
            return True
    else: return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'