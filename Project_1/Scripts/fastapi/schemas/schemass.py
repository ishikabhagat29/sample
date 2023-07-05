from sqlalchemy import float,TIMESTAMP
from pydantic import BaseModel



class value(BaseModel): 
    date_time:TIMESTAMP
    kw: float
    kwh: float
    current: float
    voltage: float

    class Config:
        orm_mode=True