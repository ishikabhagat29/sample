from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from scripts.db.createdb import SessionLocal
import uvicorn
from scripts.services.services_file import user
from scripts.db.createdb import DeclarativeBase


app=FastAPI()
app.include_router(user)
class Base(DeclarativeBase):
    pass
    
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


class Item(BaseModel): #serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool


