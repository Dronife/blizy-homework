from src.service.util.category_util import CategoryUtil
from src.repository.category_repository import category_repository
from src.repository.model_repository import model_repository
from src.model.brand import Brand
from src.model.model import Model
from src.database import db


class ModelSynchronizer:
    def __init__(self):
        self.database_session = db.get_session()

    def sync(self) -> None:
        existing_categories = category_repository.fetch_all()
        existing_models = model_repository.fetch_all()
        models_to_keep = []
        for category in existing_categories:
            model_name = CategoryUtil.extract_model_name(category.name)

            existing_model = self.get_existing_model(model_name, existing_models)
            if existing_model is not None:
                models_to_keep.append(existing_model.id)

                continue
            model = Model(name=model_name, brand_id=category.brand_id)
            self.database_session.add(model)

        db.deleteWithCondition(Model, ~Model.id.in_(models_to_keep))
        self.database_session.commit()

    def get_existing_model(self, model_name: str, existing_models: list[Model]) -> Model | None:
        for existing_model in existing_models:
            if existing_model.name == model_name:
                return existing_model
        return None


model_synchronizer = ModelSynchronizer()
