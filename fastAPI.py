from fastapi import FastAPI
from typing import Optional
from enum import Enum
from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello" : "World"}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/food/{food_name}")
async def get_food(food_name : FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message" : "you are healty"}
    
    if food_name.value == "fruits":
        return {"food_name":food_name, "message": "you are still healty"}
    
    return {"food_name": food_name, "message" :  "you must have chosen dairy right?"}

@app.get("/items/{item_id}")
async def read_item(item_id : int, q : Optional[str] = None, short : bool = False):
    item = {"item_id":item_id}
    if q:
       item.update({"q":q})
    if not short: 
        item.update({
            "description" : "short is False"
        })
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id : int, item_id : int, q:Optional[str] = None, short : bool = False):
    item ={"item_id" : item_id, "owner_id" : user_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update({
            "description" :  "short is False"
        })
    return item

class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None

@app.post("/items")
async def create_item(item: Item):
    return item