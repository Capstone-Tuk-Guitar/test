from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MusicFile(Base):
    __tablename__ = 'music_files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255), nullable=False)
    path = Column(String(255), nullable=False)

DATABASE_URL = "mysql+pymysql://tuk_fastapi:1234@localhost/fastapi_db" 

engine = create_engine(DATABASE_URL, echo=True)

# 데이터베이스 테이블 생성
Base.metadata.create_all(engine)
