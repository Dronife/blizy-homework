from src.service.dto.product import Product

class CategoryProducts:
    def __init__(self, category_id: int, products: list[Product]):
        self.category_id = category_id
        self.products = products
        pass

    def __str__(self) -> str:
         return f"CategoryProducts(id={self.category_id!r}, name={len(self.products)!r})"

    def __repr__(self) -> str:
        return self.__str__()
