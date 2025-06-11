import re

class CategoryUtil:
    def __init__(self):
        pass

    @staticmethod
    def extract_brand_name(product_name: str) -> str:
        if 'iphone' in product_name:
            return 'apple'
        elif product_name.startswith('2nd-'):
            return product_name.split('-')[-1]
        else:
            return product_name

    @staticmethod
    def extract_model_name(product_name: str) -> str | None:
        cleaned = (
            product_name.lower()
            .replace('2nd-life-', '')
            .replace('2nd-', '')
            .replace('2ns-life-', '')
        )

        iphone_match = re.search(r'iphone[-\w]+', cleaned)
        if iphone_match:
            return iphone_match.group().replace('iphone-', '')

        if cleaned:
            return cleaned

        return None
