from src.repository.category_repository import category_repository
from src.repository.brand_repository import brand_repository
from src.service.util.category_bran_util import extract_brand_name

from src.database import db
from src.model.category import Category


class CategoryModifier():
    def create(self, new_category_names):
        database_session = db.get_session()

        existing_categories = category_repository.fetch_all()
        existing_brands = brand_repository.fetch_all()

        for new_category_name in new_category_names:
            existing_category = self.get_existing_category(new_category_name, existing_categories)
            if existing_category is not None:
                existing_categories.remove(existing_category)
                continue

            brand = self.get_brand(new_category_name, existing_brands)
            database_session.add(Category(name = new_category_name, brand_id = brand.id))

        for existing_category in existing_categories:
            self.unlink_category_from_brand(existing_category)
            database_session.delete(existing_category)

        database_session.commit()

    def get_brand(self, category_name, existing_brands):
        brand_name = extract_brand_name(category_name)
        for existing in existing_brands:
            if existing.name == brand_name:
                return existing
        
        return None

    def get_existing_category(self, category_name, existing_categories):
        for existing in existing_categories:
            if category_name == existing.name:
                return existing
        return None

category_modifier = CategoryModifier()