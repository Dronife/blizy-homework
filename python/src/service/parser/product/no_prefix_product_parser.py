import re
from src.service.dto.product import Product
from src.service.dto.scrapping.raw_product import RawProduct
import unicodedata

from src.service.parser.product.abstract_product_parser import AbstractProductParser


class NoPrefixProductParser(AbstractProductParser):
    def __init__(self):
        super().__init__()

    def parse(self, raw_product: RawProduct) -> Product|None:
        headline = raw_product.headline_string
        price_string = raw_product.price_string
        headline = self.cleanup_headline(headline)
        headline = self.remove_word_used(headline)

        product = Product()
        product.condition = 'Used'
        product.price = self.extract_price(price_string)

        product.grade = self.extract_grade(headline) or "NONE"
        headline = self.remove_words_grade(headline, product.grade)
        product.storage = self.extract_storage_size(headline)

        re_gb = re.compile(r'\s*\b\d+\s*GB(?:\s*/\s*\d+\s*GB)?\b\s*', re.I)
        parts = re_gb.split(headline)
        model_name = parts[0]+" "+parts[1]

        color = self.extract_color(model_name)
        if color:
            product.color = color
            model_name = model_name.replace(color + ', ', '')
            product.model = model_name
        else:
            product.model = model_name

        return product

    def extract_color(self, headline: str) -> str | None:
        match = re.search(r'([^\s,]+)(?=,)', headline, flags=re.IGNORECASE)

        if not match:
            return None

        color = match.group(1)
        if color.upper() == 'MIX':
            return None

        return color

no_prefix_product_parser = NoPrefixProductParser()
