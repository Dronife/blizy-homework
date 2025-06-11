from sqlalchemy import select

from src.database import db
from src.model.model import Model

class ModelRepository():
    def fetch_all(self):
        models = []

        session = db.get_session()

        stmt = select(Model)
        for model in session.scalars(stmt):
            models.append(model)

        return models


model_repository = ModelRepository()