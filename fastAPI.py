from fastapi import FastAPI,Query,Path,Body
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field

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

# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id : int, item:Item, q:Optional[str] = Query(None, max_length = 10)):
#     result = {"item_id" : item_id, **item.dict()}
#     if q:
#         result.update({"q" : q})
#     return result

#hidden query
@app.get("/items_hidden")
async def hidden_query_route(hidden_query: Optional[str]= Query(None, include_in_schema = False)):
    if hidden_query:
        return {"hidden_query" : hidden_query}
    return {"hidden_query" : "Not found"}

@app.get("/items_validation/{item_id}")
async def read_items_validation(
    item_id : int = Path(..., title = "The ID of the item to get"), q:Optional[str] = Query(None, alias = 'item-query')): #alias = q이름 바꾸는거
    results = {"item_id" : item_id}
    if q:
        results.update({"q":q})
    return results


# ## Body - multiple parameters

# class Item2(BaseModel):
#     name : str
#     description : Optional[str] = None
#     price : float
#     tax : Optional[float] = None

# # class User(BaseModel):
# #     username : str
# #     full_name : Optional[str] = None

# # class Importance(BaseModel):
# #     Importance : int

# @app.put("/items2/{item_id}")
# async def update_item(
#     *,
#     item_id : int = Path(..., title="The ID of the item to get",ge=0,le=150),
#     q: Optional[str] = None,
#     item: Item2 = Body(...,embed=True)
#     # user  : User,
#     # importance : int = Body(...)
#     ):
#     results = {"item_id" : item_id}
#     if q:
#         results.update({"q":q})
#     if item:
#         results.update({"item" : item})
#     # if user:
#     #     results.update({"user": user})
#     # if importance:
#     #     results.update({"importance" : importance})
#     return results     


# body - nested models

# class Image(BaseModel):
#     url : str
#     name : str

# class Item2(BaseModel):
#     name : str
#     description : Optional[str] = None
#     price : float
#     tax : Optional[float] = None
#     tags : set[str] = [] ##중복typing 제외
#     image : Optional[Image] = None
    

# class Offer(BaseModel):
#     name : str
#     description : Optional[str] = None
#     price: float
#     items: list[Item2]

# @app.put("/items/{item_id}")
# async def update_item(item_id : int, item : Item2):
#     results = {"item_id" : item_id, "item" : item}
#     return results

# @app.post("/offers")
# async def create_offer(offer: Offer):
#     return offer

# @app.post("/images/multiple")
# async def create_multiple_images(images : list[Image] = Body(..., embed = True)):
#     return images

# @app.post("/blah")
# async def create_some_blahs(blahs : dict[int,float]):
#     return blahs

# Declare Request Example Data
class Item2(BaseModel):
    name : str = Field(..., example = "Foo")
    description : Optional[str] = Field(None, example="A very nice Item")
    price : float = Field(..., exameple = 16.25)
    tax : Optional[float] = Field(None, example = 1.67)

#아래 주석을 헤제하고 위의 Filed를 없애는 경우와 같은 결과
    # class Config:
    #     json_schema_extra ={
    #         "example" : {
    #             "name" : "Foo",
    #             "description" : "A very nice Item",
    #             "price" : 16.25,
    #             "tax" : 1.67
    #         }
    #     }

@app.put("/items/{item_id}")
async def update_item(item_id : int, item : Item2):
    results = {"item_id" : item_id, "item" : item}
    return results