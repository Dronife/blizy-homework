import re
from src.service.dto.product import Product
from src.service.dto.scrapping.raw_product import RawProduct
import unicodedata

class AbstractProductParser:
    def __init__(self):
        pass

    def cleanup_headline(self, headline: str) -> str:
        headline = unicodedata.normalize("NFKC", headline)
        headline = re.sub(r'[\u00A0\u202F\u200B]', ' ', headline)
        headline = headline.replace('В', ' ')

        return headline

    def remove_word_used(self, headline: str) -> str:
        return re.sub(r',\s*used\b', '', headline, flags=re.I)

    def remove_words_grade(self, headline: str, grade: str) -> str:
        headline = re.sub(rf", Grade {re.escape(grade)}", '', headline, flags=re.IGNORECASE)
        headline = re.sub(rf", {re.escape(grade)} Grade", '', headline, flags=re.IGNORECASE)

        return headline

    def extract_price(self, price_string):
        return float(price_string.replace("\xa0", '').replace(',', '.'))

    def extract_grade(self, headline: str) -> str:
        re_grade_prefix = re.compile(r'\bGrade\s*(A\+?|AB|B|C|D)\b', re.I)
        re_grade_suffix = re.compile(r'\b(A\+?|AB|B|C|D)\s*Grade\b', re.I)

        grade = re_grade_prefix.search(headline) or re_grade_suffix.search(headline)

        return grade.group(1).upper() if grade else None

    def extract_storage_size(self, text: str) -> int | None:
        re_size = re.compile(r'(\d+)\s*(?:GB|TB)', re.I)  # match “number GB” or “number TB”
        nums = re_size.findall(text)

        return int(nums[-1]) if nums else None