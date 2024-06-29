from typing import Union
from fastapi import FastAPI
from enum import Enum

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id : int, q : Union[str,None] = None):
    return {"item_id" : item_id, "q":q}    

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
