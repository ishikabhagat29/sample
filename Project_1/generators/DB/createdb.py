from Project_1.generators.DB.db import base,engine
from sqlalchemy import Column,Float,TIMESTAMP
print("Creating database ....")
class postgres(base):
    __tablename__='numbers'
    date_time=Column(TIMESTAMP,nullable=False)
    kw=Column(Float,nullable=False,primary_key=True)
    kwh=Column(Float,nullable=False)
    current=Column(Float,nullable=False)
    voltage=Column(Float,nullable=False)
    
base.metadata.create_all(engine)