from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True})

templates = Jinja2Templates(directory='templates')
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})


@app.post('/user/{username}/{age}')
async def register_user(username: Annotated[str, Path(min_length=2,
                                                      max_length=20,
                                                      description='Enter your username')],
                        age: Annotated[int, Path(ge=18,
                                                 le=90,
                                                 description='Enter your age')]) -> User:
    new_id = len(users) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1,
                                                   le=100,
                                                   description='Enter your ID')],
                      username: Annotated[str, Path(min_length=2,
                                                    max_length=20,
                                                    description='Enter your username')],
                      age: Annotated[int, Path(ge=18,
                                               le=90,
                                               description='Enter your age')]) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                                   le=100,
                                                   description='Enter User ID')]) -> User:
    user_id -= 1
    try:
        deleted_user = users.pop(user_id)
        return deleted_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')
