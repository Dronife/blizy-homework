from src.model.product import Product
from hashlib import md5

class ProductModelUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_hash(product: Product) -> str:
        modelName = product.model.name if product.model else ""
        raw = f"{modelName}|{product.grade.value}|{product.condition.value}|{product.storage}|{product.color}".lower()

        return md5(raw.encode()).hexdigest()