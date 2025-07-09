numbers = int(input("Введіть 4-х значне число: "))

num4 = numbers % 10
prep_num = numbers // 10

num3 = prep_num % 10
prep_num2 = prep_num // 10

num2 = prep_num2 % 10
prep_num3 = prep_num2 // 10

num1 = prep_num3 % 10

print(num1)
print(num2)
print(num3)
print(num4)