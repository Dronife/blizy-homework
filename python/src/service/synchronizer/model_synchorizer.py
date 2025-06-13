from src.service.dto.category_products import CategoryProducts
from src.service.dto.product import Product
from src.service.util.category_util import CategoryUtil
from src.repository.category_repository import category_repository
from src.repository.model_repository import model_repository
from src.repository.product_repository import product_repository
from src.model.brand import Brand
from src.model.model import Model
from src.model.product import Product
from src.database import db

class ModelSynchronizer:
    def __init__(self):
        self.database_session = db.get_session()

    def sync_from_products(self, category_products: list[CategoryProducts]) -> None:
        models_to_keep = []
        all_new_names = []
        for category_product in category_products: #type: CategoryProducts
            new_model_names = []
            existing_models = model_repository.fetch_all_by_category_id(category_product.category_id)
            for existing_model in existing_models:
                all_new_names.append(existing_model.name)

            for product in category_product.products: #type: Product
                model_name = product.model
                existing_model = self.get_existing_model(model_name, existing_models)
                if existing_model is not None:
                    models_to_keep.append(existing_model.id)

                    continue

                new_model_names.append(model_name)

            unique_new_names = self.get_unique_names(new_model_names, all_new_names)
            print("Unique model names: ", unique_new_names, " category_id: ", category_product.category_id)
            # exit()
            for model_name in unique_new_names:
                model = Model(name = model_name, category_id = category_product.category_id)
                self.database_session.add(model)

            all_new_names = all_new_names + list(unique_new_names)

        self.database_session.commit()

        if models_to_keep:
            db.deleteWithCondition(Product, ~Product.model_id.in_(models_to_keep))
            db.deleteWithCondition(Model, ~Model.id.in_(models_to_keep))

    def get_unique_names(self, new_names: list[str], all_names: list[str])-> set[str]:
        unique_names = []
        for new_name in new_names:
            if new_name in all_names:
                continue
            unique_names.append(new_name)

        return set(unique_names)

    def get_existing_model(self, model_name: str, existing_models: list[Model]) -> Model | None:
        for existing_model in existing_models:
            if existing_model.name == model_name:
                return existing_model
        return None


model_synchronizer = ModelSynchronizer()
