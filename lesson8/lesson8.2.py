import string

def is_palindrome(text: str) -> bool:
    low_text = text.lower()
    clean_text = ""
    for el in text.lower():
        if el in string.ascii_letters + string.digits:
            clean_text += el
    return clean_text == clean_text[::-1]