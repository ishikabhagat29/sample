from scripts.schemas.user_schema import Item
from scripts.db.createdb import DeclarativeBase
from fastapi import status,HTTPException
from scripts.db.createdb import SessionLocal
from fastapi import APIRouter
from scripts.schemas.user_schema import Item
from scripts.models.models import Item1



user = APIRouter()
db = SessionLocal()
class Base(DeclarativeBase):
    pass


class handling:
    def get_all_items():
        """A function to get all the details of the items
         return: empty array"""
        try:
          return(db.query(Item1).all())
        except Exception as e:
            print(e)
    def get_an_item(item_id:int):
        """A function to get details of a particular item
        return:details of an item"""
        try:
          return(db.query(Item1).filter(Item1.id==item_id).first())
        except Exception  as e:
           print(e)
    def create_an_item(item:Item):
        try:
            db_item=db.query(Item1).filter(Item1.name==item.name).first()

            if db_item is not None:
                raise HTTPException(status_code=400,detail="Item already exists")
    
            new_item=Item1(
                name=item.name,
                price=item.price,
                description=item.description,
                on_offer=item.on_offer
            )

            db.add(new_item)
            db.commit()

            return new_item
        except Exception as e:
            print(e)
    def update_an_item(item_id:int,item:Item):
        """A function to create a new item 
       param: items
       return: it returns the data in response body"""
        try:
            item_to_update=db.query(Item1).filter(Item1.id==item_id).first()
            item_to_update.name=item.name
            item_to_update.price=item.price
            item_to_update.description=item.description
            item_to_update.on_offer=item.on_offer

            db.commit()

            return item_to_update
        except Exception as e:
            print(e)
    def delete_item(item_id:int):
        """A function to update details of an item
        params : items
        return : updated data of an item """
        try:
            item_to_delete=db.query(Item1).filter(Item1.id==item_id).first()

            if item_to_delete is None:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
            db.delete(item_to_delete)
            db.commit()

            return item_to_delete
        except Exception as e:
            print(e)  






        



