from createdb import Base, engine
#from scripts.models.models import Item
from sqlalchemy import String,Boolean,Integer,Column,Text
from sqlalchemy import create_engine


print("Creating database ....")

Base.metadata.create_all(engine)


    
class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    price=Column(Integer,nullable=False)
    on_offer=Column(Boolean,default=False)
print("finish")


Base.metadata.create_all(engine)

