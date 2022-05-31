from fastapi import FastAPI
from models import User
from database import engine


app = FastAPI()


@app.get('/users')
async def get_all_users():
    pass


@app.post('/users')
async def create_an_user():
    pass


@app.get('/user/{user_id}')
async def get_an_user(user_id: int):
    pass


@app.put('/user/{user_id}')
async def update_an_user(user_id: int):
    pass


@app.delete('/user/{user_id}')
async def delete_an_user(user_id: int):
    pass