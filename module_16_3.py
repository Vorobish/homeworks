from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')
                    , age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str = Path(min_length=1, max_length=3, description='Enter user_id', example='1')
                      , username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')
                      , age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str = Path(min_length=1, max_length=3, description='Enter user_id', example='1')) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'


# python -m uvicorn module_16_3:app

# При вызове НЕ из docs работает только если все команды поменять на @app.get
# http://127.0.0.1:8000/users
# http://127.0.0.1:8000/user/UrbanUser/24
# http://127.0.0.1:8000/user/NewUser/22
# http://127.0.0.1:8000/user/1/UrbanProfi/28
# http://127.0.0.1:8000/user/2















