from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey

from src.model.base import Base

class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id"))

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r}, brand_id={self.brand_id!r})"