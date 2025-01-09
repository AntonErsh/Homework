from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{username}/{age}')
async def info_user(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  description='Enter your username')],
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             description='Enter your age')]) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age} '


@app.get('/user/{user_id}')
async def number_user(user_id: Annotated[int, Path(ge=1,
                                                   le=100,
                                                   description='Enter User ID')]) -> str:
    return f'Вы вошли как пользователь №{user_id} '
