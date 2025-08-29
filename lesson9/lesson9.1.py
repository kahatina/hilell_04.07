def popular_words (text: str, words: list) -> dict:

    low_text = text.lower()
    lst_low_text = low_text.split()
    result = {}

    for word in words:
        lst_low_text.count(word)
        result[word] = lst_low_text.count(word)

    return result