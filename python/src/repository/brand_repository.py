from sqlalchemy import select

from src.database import db
from src.model.brand import Brand

class BrandRepository():
    def fetch_all(self):
        brands = []

        session = db.get_session()

        stmt = select(Brand)
        for brand in session.scalars(stmt):
            brands.append(brand)

        return brands


brand_repository = BrandRepository()