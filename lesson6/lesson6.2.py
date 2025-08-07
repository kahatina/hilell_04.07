user_number = int(input("Введіть число від 0 до 8640000: "))

if user_number < 0 or user_number > 8640000:
    print("Невірне число")
else:
    find_seconds = divmod(user_number, 60)
    seconds = find_seconds[1]

    find_minutes = divmod(find_seconds[0], 60)
    minutes = find_minutes[1]

    find_hours = divmod(find_minutes[0], 24)
    hours = find_hours[1]
    days = find_hours[0]

    last_number = days % 10
    last_two_numbers = days % 100

    if last_two_numbers in range(11, 15):
        word_day = "днів"
    elif last_number == 1:
        word_day = "день"
    elif last_number in range(2, 5):
        word_day = "дні"
    else:
        word_day = "днів"

    new_sec = str(seconds).zfill(2)
    new_min = str(minutes).zfill(2)
    new_hours = str(hours).zfill(2)

    print(f"{days} {word_day}, {new_hours}:{new_min}:{new_sec}")