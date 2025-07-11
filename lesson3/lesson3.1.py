num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
act = input("Введіть дію: ")

if act == "+":
    result = num1 + num2
elif act == "-":
    result = num1 - num2
elif act == "*":
    result = num1 * num2
elif act == "/":
    if num2 == 0:
        result = "Не можна ділити на 0"
    else:
        result = num1 / num2
print(result)