from fastapi import FastAPI, status, Body, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def post_user(user: User
                    , username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')
                    , age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> User:
    i = 0
    if len(users) == 0:
        i = 1
    else:
        list_ = []
        for j in users:
            list_.append(j.id)
        i = max(list_) + 1
    user.id = i
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=1, le=10, description='Enter user_id', example='1')
                      , username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')
                      , age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
        else:
            raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=10, description='Enter user_id', example='1')):
    for user in users:
        if user.id == user_id:
            a = user
            users.remove(user)
            return a
    else:
        raise HTTPException(status_code=404, detail="User was not found")


# python -m uvicorn module_16_4:app









