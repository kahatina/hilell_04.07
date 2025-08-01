import string

line = input("Введіть речення: ")

clean_line = ""
for char in line:
    if char not in string.punctuation:
        clean_line += char

big_line = clean_line.title()
plain_line = big_line.replace(" ", "")
hashtag = "#" + plain_line

if len(hashtag) >= 140:
    print(hashtag[:140])
else:
    print(hashtag)