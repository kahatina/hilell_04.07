import keyword
import string

line = input("Введіть рядок: ")
result = True

if not line:
    result = False

if line[0].isdigit():
    result = False

if not line.islower():
    result = False

if line in keyword.kwlist:
    result = False

if " " in line:
    result = False

new_ban_list = string.punctuation.replace('_', '')
for char in line:
    if char in new_ban_list:
        result = False

if line.count("_") > 1:
    result = False