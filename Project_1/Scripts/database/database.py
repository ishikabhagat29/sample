from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Scripts.publisher.publisher import publisher
sql_url = "postgresql://postgres:1234@localhost/project_db"
print(sql_url)
engine=create_engine(url = sql_url,
    echo=True
)

class Base(DeclarativeBase):
    pass
SessionLocal=sessionmaker(bind=engine)
