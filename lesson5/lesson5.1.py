import keyword
import string

line = input("Введіть рядок: ")
result = True

if not line:
    result = False

if line[0].isdigit():
    result = False

if any(с.isupper() for c in line):
    result = False

if line in keyword.kwlist:
    result = False

if " " in line:
    result = False

if "__" in line:
    result = False

new_ban_list = string.punctuation.replace('_', '')
for char in line:
    if char in new_ban_list:
        result = False

print(result)