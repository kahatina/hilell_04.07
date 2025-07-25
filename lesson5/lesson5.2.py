while True:

    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    action = input("Введіть дію: ")

    if action == "+":
        result = number1 + number2
    elif action == "-":
        result = number1 - number2
    elif action == "*":
        result = number1 * number2
    elif action == "/":
        if number2 == 0:
            result = "Не можна ділити на 0"
        else:
            result = number1 / number2

    print(result)

    answer = input("Продовжити обчислення? ")
    if answer.lower() == "yes":
        continue
    else:
        break