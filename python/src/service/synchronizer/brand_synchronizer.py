from src.service.util.category_util import CategoryUtil
from src.repository.brand_repository import brand_repository
from src.model.brand import Brand
from src.database import db

class BrandSynchronizer:
    def __init__(self):
        self.database_session = db.get_session()

    def sync(self, new_category_names: str) -> None:
        appended_brands = []
        existing_brands = brand_repository.fetch_all()
        brands_to_keep = []
        for new_category_name in new_category_names:
            brand_name = CategoryUtil.extract_brand_name(new_category_name)
            existing_brand = self.get_existing_brand(brand_name, existing_brands)
            if existing_brand is not None:
                brands_to_keep.append(existing_brand.id)
                continue

            if brand_name in appended_brands:
                continue

            appended_brands.append(brand_name)
            self.database_session.add(Brand(name=brand_name))

        db.deleteWithCondition(Brand, ~Brand.id.in_(brands_to_keep))

        self.database_session.commit()

    def get_existing_brand(self, brand_name: str, existing_brands: list[Brand]) -> Brand | None:
        for existing in existing_brands:
            if brand_name == existing.name:
                return existing
        return None


brand_synchronizer = BrandSynchronizer()