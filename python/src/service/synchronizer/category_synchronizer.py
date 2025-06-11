from src.repository.category_repository import category_repository
from src.repository.brand_repository import brand_repository
from src.service.util.category_util import CategoryUtil
from src.model.brand import Brand
from src.model.category import Category
from src.database import db

class CategorySynchronizer:
    def __init__(self):
        self.database_session = db.get_session()

    def sync(self, new_category_names: list[str]) -> None:
        existing_categories = category_repository.fetch_all()
        existing_brands = brand_repository.fetch_all()
        categories_to_keep = []

        for new_category_name in new_category_names:
            existing_category = self.get_existing_category(new_category_name, existing_categories)
            if existing_category is not None:
                categories_to_keep.append(existing_category.id)
                continue

            brand = self.get_brand(new_category_name, existing_brands)
            self.database_session.add(Category(name=new_category_name, brand_id=brand.id))


        db.deleteWithCondition(Category, ~Category.id.in_(categories_to_keep))

        self.database_session.commit()

    def get_brand(self, category_name: str, existing_brands: list[Brand]) -> Brand | None:
        brand_name = CategoryUtil.extract_brand_name(category_name)
        for existing in existing_brands:
            if existing.name == brand_name:
                return existing

        return None

    def get_existing_category(self, category_name: str, existing_categories: list[Category]) -> Category | None:
        for existing in existing_categories:
            if category_name == existing.name:
                return existing
        return None


category_synchronizer = CategorySynchronizer()