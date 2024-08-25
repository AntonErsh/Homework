def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
        if i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'Richiest', 'oriChalCum', 'cHEers', 'rICHies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Домашний', "Дом", "Домра", "Домен")
print(result1)
print(result2)
print(result3)