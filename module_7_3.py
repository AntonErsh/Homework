import string


class WordsFinder:
    def __init__(self, *file_name: str):
        self.file_names = [*file_name]

    def get_all_words(self) -> dict:
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                table = str.maketrans('', '', string.punctuation)
                list_for_update = []
                for i in file:
                    i = i.lower().translate(table).split()
                    list_for_update.extend(i)
                all_words.update({file_name: list_for_update})
        return all_words

    def find(self, word: str) -> dict:
        dict_result = {}
        for key, value in self.get_all_words().items():
            count = 1
            for i in value:
                if word == i:
                    dict_result.update({key: count})
                    break
                count += 1
        return dict_result

    def count(self, word: str) -> dict:
        dict_result = {}
        for key, value in self.get_all_words().items():
            count = 0
            for i in value:
                if word == i:
                    count += 1
            dict_result.update({key: count})
        return dict_result


result = WordsFinder(
    'Walt Whitman - O Captain! My Captain!.txt',
    'Rudyard Kipling - If.txt',
    'Mother Goose - Monday’s Child.txt'
)
print(result.get_all_words())
print(result.find('the'))
print(result.count('the'))
