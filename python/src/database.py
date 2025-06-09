import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlalchemy import select

from src.model.product import Product

load_dotenv()
print(__name__)

class Database:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def get_session(self):
        return self.SessionLocal()
    
    def get_table_names(self):
        inspector = inspect(db.engine)
        return inspector.get_table_names()

db = Database()

