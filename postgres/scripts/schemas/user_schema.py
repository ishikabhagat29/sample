from sqlalchemy.sql.expression import null
# from sqlalchemy import String,Boolean,Integer,Column,Text
from pydantic import BaseModel




class Item(BaseModel): 
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode=True



