from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    user_id: str
    user_name: str


"""
PUT

{
    "item": {
        "name": "ssd",
        "description": "손소독",
        "price": 15.5,
        "tax": 3.2
    },
    "user": {
        "user_id": "ssd1234",
        "user_name": "asdf"
    },
    "importance": 111
}
"""


@app.put('/item/{item_id}')
async def update_item(
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(...)
):
    result = {"item_id": item_id, "item": item, "user": user, "importance": importance}

    return result
