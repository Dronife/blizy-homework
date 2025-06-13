from sqlalchemy import select

from src.database import db
from src.model.product import Product

class ProductRepository():
    def fetch_all_by_category_id(self, category_id: int)->list[Product]:
         products = []
         stmt = select(Product).where(Product.category_id == category_id)
         for product in db.get_session().scalars(stmt):
             products.append(product)

         return products


product_repository = ProductRepository()