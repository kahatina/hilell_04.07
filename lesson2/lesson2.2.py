numbers = int(input("Введіть 5-ти значне число: "))

num5 = numbers % 10
prep_num = numbers // 10

num4 = prep_num % 10
prep_num2 = prep_num // 10

num3 = prep_num2 % 10
prep_num3 = prep_num2 // 10

num2 = prep_num3 % 10
prep_num4 = prep_num3 // 10

num1 = prep_num4 % 10

print((num5 * 10000) + (num4 * 1000) + (num3 * 100) + (num2 * 10) + num1)