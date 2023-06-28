from scripts.schemas.user_schema import Item
from scripts.db.createdb import DeclarativeBase
from fastapi import status,HTTPException
from scripts.db.createdb import SessionLocal
from fastapi import APIRouter
from scripts.schemas.user_schema import Item
from scripts.models.models import Item1
from scripts.core.handlers.handlers import handling


user = APIRouter()
db = SessionLocal()
class Base(DeclarativeBase):
    pass
 


@user.get('/items',)
def get_all_items():
    """A function to get all the details of the items
         params: items
         return: empty array"""
    try:
       handling.get_all_items()
    except Exception as e:
        print(e)

@user.get('/item/')
def get_an_item(item_id:int):
    """A function to get details of a particular item
        params: items
        return:details of an item"""
    try:
          resp= handling.get_an_item()
          return resp
    except Exception as e:
        print(e)

@user.post('/items')
def create_an_item(item:Item):
    """A function to create a new item 
       param: items
       return: it returns the data in response body"""
    try:
        resp = handling.create_an_item(Item)
        return (Item)
    except Exception as e:
        print(e)

@user.put('/item/')
def update_an_item(item_id:int,item:Item):
    """A function to update details of an item
        params : items
        return : updated data of an item """
    try:
          resp = handling.update_an_item(Item)
          return resp
    except Exception as e:
       print(e)

@user.delete('/item/')
def delete_item(item_id:int):
    """A function to delete an item 
        params: items
        return: data after deleting an item"""
    try:
         resp = handling.delete_item(Item)
         return resp
    except Exception as e:
       print(e)
