from sqlalchemy import select

from src.database import db
from src.model.category import Category

class CategoryRepository():
    def fetch_all(self):
         products = []

         stmt = select(Category)
         for product in db.get_session().scalars(stmt):
             products.append(product)

         return products


category_repository = CategoryRepository()