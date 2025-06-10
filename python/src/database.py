import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlalchemy import delete

load_dotenv()

class Database:
    _instance = None
    _engine = None
    _SessionLocal = None
    _Base = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_once()
        return cls._instance

    def _init_once(self):
        self.database_url = os.getenv("DATABASE_URL")

        if Database._engine is None:
            Database._engine = create_engine(
                self.database_url,
                pool_pre_ping=True,
                future=True,
            )

            Database._SessionLocal = scoped_session(
                sessionmaker(
                    bind=Database._engine,
                    autoflush=False,
                    autocommit=False,
                    expire_on_commit=False,
                )
            )

            Database._Base = declarative_base()

        self.engine = Database._engine
        self.SessionLocal = Database._SessionLocal
        self.Base = Database._Base

    def deleteWithCondition(self, className, condition):
        stmt = delete(className).where(condition)
        self.get_session().execute(stmt)

    def get_session(self):
        return self.SessionLocal()

    def remove_session(self):
        self.SessionLocal.remove()

    def get_table_names(self):
        inspector = inspect(self.engine)
        return inspector.get_table_names()


db = Database()
