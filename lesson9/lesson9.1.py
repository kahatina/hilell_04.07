def popular_words (text: str, words: list) -> dict:

    low_text = text.lower()
    lst_low_text = low_text.split()
    result = {}

    for word in words:
        lst_low_text.count(word)
        result[word] = lst_low_text.count(word)

    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')