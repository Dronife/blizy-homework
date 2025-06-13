from src.service.parser.product.default_product_parser import default_product_parser
from src.service.parser.product.no_prefix_product_parser import no_prefix_product_parser
from src.service.dto.product import Product
from src.service.dto.scrapping.raw_product import RawProduct

class ProductParserFacade:
    def __init__(self):
        pass

    def parse(self, raw_product: RawProduct) -> Product|None:
        if "USED" in raw_product.headline_string and "Smartphone" not in raw_product.headline_string:
            return no_prefix_product_parser.parse(raw_product)
        return default_product_parser.parse(raw_product)

product_parser = ProductParserFacade()