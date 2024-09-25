import time


class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return self.nickname


class Video:
    time_now = 0

    def __init__(self, title, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname: str, password) -> str:
        for i in self.users:
            if nickname in i.nickname:
                if hash(password) == i.password:
                    self.current_user = i
                    return f'Вход выполнен, {nickname}'
                else:
                    return 'Неверное имя пользователя или пароль'

    def register(self, nickname: str, password, age: int) -> str:
        user_register = User(nickname, password, age)
        if len(ur.users) > 0:
            for i in ur.users:
                if nickname not in i.nickname:
                    ur.users.append(user_register)
                    ur.log_in(nickname, password)
                    return f'Пользователь {nickname} зарегистрирован '
                else:
                    return f'Пользователь {nickname} уже существует '
        else:
            ur.users.append(user_register)
            ur.log_in(nickname, password)
            return f'Пользователь {nickname} зарегистрирован '

    def log_out(self) -> str:
        ur.current_user = None
        return 'Вы вышли из аккаунта'

    def add(self, *args: Video) -> None:
        list_to_add = [*args]
        if len(ur.videos) > 0:
            for i in ur.videos:
                if args not in i.title:
                    for j in list_to_add:
                        ur.videos.append(j)
                else:
                    return
        else:
            for j in list_to_add:
                ur.videos.append(j)

    def get_videos(self, search_word: str) -> list:
        search_word = search_word.lower()
        list_of_videos = []
        for i in ur.videos:
            title_lower = i.title.lower()
            if search_word in title_lower:
                list_of_videos.append(i)
        return list_of_videos

    def watch_video(self, name_film: str) -> None:
        for i in self.videos:
            if not self.current_user:
                print("Войдите в аккаунт, чтобы смотреть видео")
                return
            if self.current_user.age < 18 and i.adult_mode is True:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            if name_film == i.title:
                for j in range(i.duration + 1):
                    time.sleep(0.05)
                    print(j)
                print('Конец видео')
                return


ur = UrTube()
print(ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55))
print(ur.log_out())
print(ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi'))
print(ur.current_user)
v1 = Video('Лучший язык программирования 2024 года', 20)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.videos)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
print(ur.register('vasya_pupkin', 'lolkekcheburek', 13))
ur.watch_video('Для чего девушкам парень программист?')
print(ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 17))
ur.watch_video('Для чего девушкам парень программист?')
print(ur.log_in('vasya_pupkin', 'F8098FM8fjm9mi'))
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024')
