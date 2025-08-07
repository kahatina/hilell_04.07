import string

user_intent = input("Введіть діапазон літер: ")

user_intent_list = user_intent.split("-")

first_letter = user_intent_list[0]
last_letter = user_intent_list[1]

index_first_letter = string.ascii_letters.index(first_letter)
index_last_letter = string.ascii_letters.index(last_letter) + 1

print(string.ascii_letters[index_first_letter:index_last_letter])