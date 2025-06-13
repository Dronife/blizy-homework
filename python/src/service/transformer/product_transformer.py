from src.model.product import Product as ProductModel
from src.model.model import Model
from src.service.dto.product import Product as ProductDto
from src.enumerators.condition import ConditionEnum
from src.enumerators.grade import GradeEnum
from src.repository.model_repository import model_repository

class ProductTransformer:
    _model_cache: list[ProductModel] | None = None
    def __init__(self):
        if ProductTransformer._model_cache is None:
            ProductTransformer._model_cache = model_repository.fetch_all()

    def get_model(self, model_string: str) -> Model | None:
        print("Model string: ", model_string)
        for model in ProductTransformer._model_cache:
            if model_string == model.name:
                return model
        return None

    def dto_to_model(self, dto: ProductDto, existing: ProductModel|None = None) -> ProductModel | None:
        product = ProductModel() if existing is None else existing

        model = self.get_model(dto.model) #type:Model or None

        product.grade = GradeEnum.get_from_string(dto.grade)
        product.price = dto.price
        product.condition = ConditionEnum.get_from_string(dto.condition)
        product.model_id = model.id if model else None
        product.category_id = model.category_id if model else None
        product.color = dto.color
        product.storage = dto.storage

        return product

product_transformer = ProductTransformer()