from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sql_url = "postgresql://postgres:1234@localhost/my_db"
print(sql_url)
engine=create_engine(url = sql_url,
    echo=True
)

class Base(DeclarativeBase):
    pass
SessionLocal=sessionmaker(bind=engine)