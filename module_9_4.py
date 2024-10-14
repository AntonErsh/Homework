from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name: str):
    def write_everything(*data_set):
        with open('file_name.txt', 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(f'{i} \n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = [*words]

    def __call__(self, *args, **kwargs):
        word_choice = choice(self.words)
        return word_choice


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Когда-нибудь', 'Этот мир абсолютно понятен', 'Хочу домой',
                        "Памагити!!!")
print(first_ball())
print(first_ball())
print(first_ball())
