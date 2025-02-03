from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://tuk_fastapi:1234@localhost/fastapi_db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(bind=engine)
