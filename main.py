from fastapi import FastAPI
from typing import Optional
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


class Model(str, Enum):
    python = "python"
    snake = "snake"
    fastapi = "fastapi"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get('/')
async def root():
    return {"message": "server is running"}


@app.get('/user/{user_id}/item/{item_id}')
async def get_user_item(
        user_id: int,
        item_id: str,
        query: Optional[str] = None,
        sh: bool = False
):
    item = {"item_id": item_id, "user_id": user_id}

    if query:
        item.update({"query": query})

    if not sh:
        item.update(
            {"description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."}
        )

    return item


@app.get('/model/{model_name}')
async def get_model(model_name: Model):
    if model_name == Model.python:
        return {"model_name": model_name, "message": "py"}

    if model_name.value == "fastapi":
        return {"model_name": model_name, "message": "fast"}

    return {"model_name": model_name, "message": "model page"}


# http://localhost:8000/item/asdf?description=asdf
@app.put('/item/{item_id}')
async def get_item(
        item_id: int,
        item: Item,
        q: Optional[str] = None
):
    result = {"item_id": item, **item.dict()}

    if q:
        result.update({"q": q})

    return result


@app.post('/item')
async def create_items(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict
