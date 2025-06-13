import re
from src.service.dto.product import Product
from src.service.dto.scrapping.raw_product import RawProduct
import unicodedata

from src.service.parser.product.abstract_product_parser import AbstractProductParser

class DefaultProductParser(AbstractProductParser):
    def __init__(self):
        pass

    def parse(self, raw_product: RawProduct) -> Product|None:
        headline = raw_product.headline_string
        price_string = raw_product.price_string

        re_prefix = re.compile(r'^\s*\S+\s+\S+\s+', re.I)
        headline = re_prefix.sub('', headline).strip()
        headline = self.cleanup_headline(headline)
        headline = self.remove_word_used(headline)

        product = Product()
        product.condition = 'Used'
        product.price = self.extract_price(price_string)

        product.grade = self.extract_grade(headline) or "NONE"
        headline = self.remove_words_grade(headline, product.grade)

        product.storage = self.extract_storage_size(headline)

        re_gb = re.compile(r'\s*\b\d+\s*(?:GB|TB)(?:\s*/\s*\d+\s*(?:GB|TB))?\b\s*', re.I)
        parts = re_gb.split(headline)

        product.model = parts[0]
        product.color = parts[1]

        return product

default_product_parser = DefaultProductParser()
