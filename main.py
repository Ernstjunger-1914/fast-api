from fastapi import FastAPI
from enum import Enum


class Model(str, Enum):
    python = "python"
    snake = "snake"
    fastapi = "fastapi"


app = FastAPI()


@app.get('/')
async def root():
    return {"message": "server is running"}


@app.get('/user/{user_id}')
async def get_user(user_id):
    return {"user_id": user_id}


@app.get('/model/{model_name}')
async def get_model(model_name: Model):
    if model_name == Model.python:
        return {"model_name": model_name, "message": "py"}

    if model_name.value == "fastapi":
        return {"model_name": model_name, "message": "fast"}

    return {"model_name": model_name, "message": "model page"}
