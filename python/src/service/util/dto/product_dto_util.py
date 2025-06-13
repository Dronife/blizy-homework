from src.service.dto.product import Product
from hashlib import md5

class ProductDtoUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_hash(product: Product) -> str:
        raw = f"{product.model}|{product.grade.upper()}|{product.condition.upper()}|{product.storage}|{product.color}".lower()

        return md5(raw.encode()).hexdigest()