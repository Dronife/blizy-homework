import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()


class Database:
    _instance = None
    _engine = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_once()
        return cls._instance

    def _init_once(self):
        # run exactly once
        self.database_url = os.getenv("DATABASE_URL")

        if Database._engine is None:
            Database._engine = create_engine(self.database_url, pool_pre_ping=True)
            Database._SessionLocal = sessionmaker(bind=Database._engine)
            Database._Base = declarative_base()

        # share the same objects on every instance
        self.engine = Database._engine
        self.SessionLocal = Database._SessionLocal
        self.Base = Database._Base

    # helper methods
    def get_session(self):
        return self.SessionLocal()

    def get_table_names(self):
        inspector = inspect(self.engine)
        return inspector.get_table_names()

db = Database()
