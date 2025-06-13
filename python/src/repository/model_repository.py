from sqlalchemy import select

from src.database import db
from src.model.model import Model

class ModelRepository():
    def fetch_all_by_category_id(self, category_id: int) -> list[Model]:
        models = []

        session = db.get_session()

        stmt = select(Model).where(Model.category_id == category_id)
        for model in session.scalars(stmt):
            models.append(model)

        return models

    def fetch_all(self) -> list[Model]:
        models = []

        session = db.get_session()

        stmt = select(Model)
        for model in session.scalars(stmt):
            models.append(model)

        return models

model_repository = ModelRepository()