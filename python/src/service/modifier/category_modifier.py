from src.repository.category_repository import category_repository
from src.database import db
from src.model.category import Category

class CategoryModifier():
    def create(self, new_categories):
        database_session = db.get_session()

        existing_categories = category_repository.fetch_all()
        for new_category in new_categories:
            if new_category in existing_categories:
                continue
            category = Category(
                name = new_category
            )

            database_session.add_all([category])

        database_session.commit()

category_modifier = CategoryModifier()