from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def register_user(username: Annotated[str, Path(min_length=2,
                                                      max_length=20,
                                                      description='Enter your username')],
                        age: Annotated[int, Path(ge=18,
                                                 le=90,
                                                 description='Enter your age')]) -> str:
    new_id = str(int(max(users, key=int)) + 1)
    users.update({new_id: f'Имя: {username}, возраст: {age}'})
    return f'User {new_id} was registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(description='Enter User ID')],
                      username: Annotated[str, Path(min_length=2,
                                                    max_length=20,
                                                    description='Enter your username')],
                      age: Annotated[int, Path(ge=18,
                                               le=90,
                                               description='Enter your age')]) -> str:
    try:
        users.update({user_id: f'Имя: {username}, возраст: {age}'})
    except KeyError:
        return f'User {user_id} not found'

    return f'The user {user_id} was updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(description='Enter User ID')]) -> str:
    try:
        users.pop(user_id)
    except KeyError:
        return f'User {user_id} not found'

    return f"The user {user_id} was deleted"
