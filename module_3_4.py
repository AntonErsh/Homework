def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
        if i.lower() in root_word.lower():
            same_words.append(i)
    print(same_words)


single_root_words('rich', 'Richiest', 'oriChalCum', 'cHEers', 'rICHies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
single_root_words('Домашний', "Дом", "Домра", "Домен")
