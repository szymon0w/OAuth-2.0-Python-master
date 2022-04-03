from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import DBConfig

SQLALCHEMY_DATABASE_URL = f'postgresql://{DBConfig.USER}:{DBConfig.PASS}@{DBConfig.HOST}:{DBConfig.PORT}/{DBConfig.NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
