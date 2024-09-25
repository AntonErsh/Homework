class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
     Класс Пользователь. Содержит атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Привет! Выбери действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Успешный вход, {login}')
                    break
                else:
                    print('Неверный пароль ')
            else:
                print('Пользователь не найден ')
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password_confirm := input('Повторите пароль: '))
            if len(password) < 8:
                print('Длина должна быть 8 символов или более')
            elif password != password_confirm:
                print('Пароли не совпадают ')
                continue
            else:
                database.add_user(user.username, user.password)
        print(database.data)
