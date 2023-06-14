from pydantic import BaseModel
from pydantic import validator
# from pydantic import Field
# from uuid import UUID, uuid4

class User(BaseModel):
    name: str
    email: str
    password: str
    # id: UUID = Field(default_factory=uuid4)


@validator('name')
def name_must_contain_space(cls, v):
    """A function to validate the name string
        params : cls,v
         return: validation error """
    try:
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()
    except Exception as e:
       print (e)



@validator('email')
def email_must_contain_space(cls, v):
    """A function to validate email
       params: cls,v
       return: validation error that the string should contain @gmail.com"""
    try:
        if ' ' not in v:
            raise ValueError('must contain @gmail.com')
        return v.title()
    except Exception as e:
       print (e)






