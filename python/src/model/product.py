from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import Enum

from src.model.base import Base
from src.enumerators.grade import GradeEnum
from src.enumerators.condition import ConditionEnum

class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    model_id: Mapped[int] = mapped_column(ForeignKey("model.id"))
    grade: Mapped[GradeEnum] = mapped_column(Enum(GradeEnum), nullable=False)
    condition: Mapped[ConditionEnum] = mapped_column(Enum(ConditionEnum), nullable=False)
    storage: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
  
    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, category_id={self.category_id!r}, brand_id={self.brand_id!r}, model_id={self.model_id!r}, condition={self.condition!r}, storage={self.storage!r}, price={self.price!r}"