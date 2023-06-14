from fastapi import APIRouter
from models.user import User
from config.db import conn
from bson import ObjectId
from schemas.user import userEntity , usersEntity
user = APIRouter()

@user.get('/find_user')
async def find_all_users():
  """ This function gets  the details of all the users  
       params: id,user
       return : users information """ 
  try:
      print(conn.local.user.find())
      print(usersEntity(conn.local.user.find()))
      return usersEntity(conn.local.user.find())
  except Exception as e:
     print(f"{str(e)}")


@user.get('/{id}')
async def find_one_user(id):
    """A function to get details of a particular user
        params : id,user
        return : details of user """
    try:
      return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))
    except Exception as e:
     print(f"{str(e)}")


@user.post('/create_user')
async def create_user(user:User):
  """A function to create a new user
      params : user
      return : returns entire database including new user"""
  try:
    resp = conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())
  except Exception as e:
     print(f"{str(e)}")



@user.put('/update_user')
async def update_user(id,user:User):
  """A function to update any one field of the details of the user
      params: id,user
      return: returns the updated field of the user"""
  try:
    resp = conn.local.user.update_one({"_id":ObjectId(id)}, {"$set": {"name" : user(user.name)}})
    conn.local.user.update_one({"_id":ObjectId(id)}, {"$set": {"name" : user(user.name)}})
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))
  except Exception as e:
     print(f"{str(e)}")
    


@user.delete('/delete_details')
async def delete_user(id,user:User):
  """A function to delete the user details
      params:id,user
      return: deletes the user details"""
  try:
    conn.local.user.find_one_and_delete({"_id":ObjectId(id)})
    return usersEntity(conn.local.user.find_one({"_id":ObjectId(id)}))
  except Exception as e:
     print(f"{str(e)}")



@user.put('/update_many')
async def update_user(id,user:User):
  """A function to update two or more field of details of the user
      params: id,user
      return: entire database with updated values"""
  try:
    conn.local.user.update_many({"_id":ObjectId(id)},{"$set":(dict(user))})
    return usersEntity(conn.local.user.update_many({"_id":ObjectId(id)}))
  except Exception as e:
     print(f"{str(e)}")


