from fastapi import FastAPI,Query
from typing import Optional
from enum import Enum
from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello" : "World"}

#Enum
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

#url parameter, q(query string), short(boolean)
@app.get("/items/{item_id}")
async def read_item(item_id : int, q : Optional[str] = Query(None, min_length=3 ,max_length=10), short : bool = False):
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

#Response Body BaseModel
class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax" : price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id : int, item:Item, q:Optional[str] = Query(None, max_length = 10)):
    result = {"item_id" : item_id, **item.dict()}
    if q:
        result.update({"q" : q})
    return result

#hidden query
@app.get("/items_hidden")
async def hidden_query_route(hidden_query: Optional[str]= Query(None, include_in_schema = False)):
    if hidden_query:
        return {"hidden_query" : hidden_query}
    return {"hidden_query" : "Not found"}