from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os

# SQLite in-memory database (no external setup needed)
DATABASE_URL="sqlite:///./test.db"

# CREATE ENGINE

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})


# sESSION AND BASE MODEL
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()


# Dependenecy to access the DB session
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
