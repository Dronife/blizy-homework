from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.model.base import Base

class Model(Base):
    __tablename__ = "model"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
  
    def __repr__(self) -> str:
        return f"Model(id={self.id!r}, name={self.name!r}"