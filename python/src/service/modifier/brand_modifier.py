from src.repository.brand_repository import brand_repository
from src.database import db
from src.model.category import Category
from src.model.brand import Brand
from src.service.util.category_bran_util import extract_brand_name

class BrandModifier():
    def __init__(self):
        self.database_session = db.get_session()

    def create(self, new_category_names):
        appended_brands = []
        existing_brands = brand_repository.fetch_all()
        keep_brands = []
        for new_category_name in new_category_names:
            brand_name = extract_brand_name(new_category_name)
            existing_brand = self.get_existing_brand(brand_name, existing_brands)
            if existing_brand is not None:
                keep_brands.append(brand_name)
                continue
            
            if brand_name in appended_brands:
                continue

            appended_brands.append(brand_name)
            self.database_session.add(Brand(name=brand_name))

        for existing in existing_brands:
            self.remove_not_existing(keep_brands)

        self.database_session.commit()

    def remove_not_existing(self, keep_brands):
        db.deleteWithCondition(Brand, ~Brand.name.in_(keep_brands))

    def get_existing_brand(self, brand_name, existing_brands):
        for existing in existing_brands:
            if brand_name == existing.name:
                return existing
        return None       

brand_modifier = BrandModifier()