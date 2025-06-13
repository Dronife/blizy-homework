from src.repository.product_repository import product_repository
from src.service.dto.category_products import CategoryProducts
from src.model.product import Product as ProductModel
from src.service.dto.product import Product as ProductDto
from src.service.util.model.product_model_util import ProductModelUtil
from src.service.util.dto.product_dto_util import ProductDtoUtil
from src.service.transformer.product_transformer import product_transformer
from src.database import db

class ProductSynchronizer:
    def __init__(self):
        self.database_session = db.get_session()
        pass

    def sync(self, category_products: list[CategoryProducts]) -> None:
        for category_product in category_products:
            existing_by_hash = self.get_exsting_products_by_hash(category_product.category_id)
            new_by_bash: dict[str, ProductDto] = {ProductDtoUtil.get_hash(n): n for n in category_product.products}
            for key, new in new_by_bash.items(): #type: dict[str, ProductDto]
                if key in existing_by_hash:
                    existing = existing_by_hash[key]
                    product_transformer.dto_to_model(new, existing)
                    existing.category_id = category_product.category_id
                    existing_by_hash.pop(key)

                    continue

                self.create(new, category_product.category_id)

            self.database_session.commit()

            ids_to_remove = [v.id for k, v in existing_by_hash.items()]
            db.deleteWithCondition(ProductModel, ProductModel.id.in_(ids_to_remove))

    def get_exsting_products_by_hash(self, category_id: int) -> dict[str, ProductModel]:
        existing_products = product_repository.fetch_all_by_category_id(category_id)

        return {ProductModelUtil.get_hash(e): e for e in existing_products}

    def create(self, new: ProductDto, category_id: int) -> None:
        product = product_transformer.dto_to_model(new)
        product.category_id = category_id
        self.database_session.add(product)

product_synchronizer = ProductSynchronizer()